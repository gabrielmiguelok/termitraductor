"""Adaptadores de motores de traducción.

Añade aquí nuevas implementaciones cumpliendo el contrato `Translator`.
"""

from __future__ import annotations

import contextlib
from typing import Protocol

import torch
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

from .config import BEAM_SIZE, CPU_THREADS, MAX_NEW_TOKENS
from .dto import TranslationRequest, TranslationResponse

__all__ = ["Translator", "HFSeq2SeqTranslator"]


class Translator(Protocol):
    """Contrato (ISP) para cualquier motor de traducción."""

    def translate(self, req: TranslationRequest) -> TranslationResponse:  # noqa: D401
        """Traduce las líneas pasadas en `req` y devuelve las traducciones."""
        ...


class HFSeq2SeqTranslator:
    """Adaptador para modelos *Hugging Face* Seq2Seq en CPU.

    - Sin herencia (composición > herencia).
    - `torch.quantization.quantize_dynamic` para reducir RAM.
    """

    def __init__(self, model_id: str) -> None:
        torch.set_num_threads(CPU_THREADS)
        torch.set_num_interop_threads(1)

        self._tokenizer = AutoTokenizer.from_pretrained(model_id)
        raw_model = AutoModelForSeq2SeqLM.from_pretrained(model_id)
        self._model = (
            torch.quantization.quantize_dynamic(
                raw_model, {torch.nn.Linear}, dtype=torch.qint8
            )
            .to("cpu")
            .eval()
        )

    @torch.inference_mode()
    def translate(self, req: TranslationRequest) -> TranslationResponse:
        if not req.lines:  # Fail‑fast
            return TranslationResponse([])

        enc = self._tokenizer(
            req.lines,
            return_tensors="pt",
            padding=True,
            truncation=True,
            max_length=MAX_NEW_TOKENS,
        )

        with contextlib.suppress(torch.no_grad):  # seguridad extra
            gen = self._model.generate(
                **{k: v.to("cpu") for k, v in enc.items()},
                num_beams=BEAM_SIZE,
                max_new_tokens=MAX_NEW_TOKENS,
            )

        dec = self._tokenizer.batch_decode(gen, skip_special_tokens=True)
        return TranslationResponse(list(dec))
