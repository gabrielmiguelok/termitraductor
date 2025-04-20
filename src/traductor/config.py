"""Parámetros de configuración inmutables (SSOT)."""

from typing import Final

DEFAULT_MODEL: Final[str] = "Helsinki-NLP/opus-mt-{src}-{tgt}"
CPU_THREADS: Final[int] = 4
MAX_NEW_TOKENS: Final[int] = 128
BEAM_SIZE: Final[int] = 2
