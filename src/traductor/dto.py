"""DTOs puros y sin lógica de negocio."""

from dataclasses import dataclass
from typing import Sequence, List

__all__ = ["TranslationRequest", "TranslationResponse"]


@dataclass(frozen=True, slots=True)
class TranslationRequest:
    """Petición de traducción: lista de líneas fuente."""
    lines: Sequence[str]


@dataclass(frozen=True, slots=True)
class TranslationResponse:
    """Respuesta de traducción: lista de líneas traducidas."""
    translated: List[str]
