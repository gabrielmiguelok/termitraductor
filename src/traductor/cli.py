"""Punto de entrada CLI.

Mantiene separado el arranque de la lógica (SRP).
"""

from __future__ import annotations

import sys
from typing import Tuple

from .config import DEFAULT_MODEL
from .translator import HFSeq2SeqTranslator
from .tui import TranslateApp


def _parse_pair(arg: str) -> Tuple[str, str]:
    """Parsea '<src>-<tgt>' → ('src', 'tgt').  Falla explícitamente."""
    try:
        return tuple(arg.lower().split("-"))  # type: ignore[return-value]
    except ValueError:
        sys.exit("❌  Formato del par de idiomas: SRC-TGT (ej. en-es)")


def main() -> None:  # noqa: D401
    """Arranca la TUI."""
    if len(sys.argv) == 2 and sys.argv[1] in {"-h", "--help"}:
        print("Uso: traductor [<SRC-TGT>]\nEj: traductor en-es")
        sys.exit(0)

    src, tgt = _parse_pair(sys.argv[1]) if len(sys.argv) >= 2 else ("en", "es")
    model_id = DEFAULT_MODEL.format(src=src, tgt=tgt)

    print(f"📥  Cargando modelo '{model_id}' (CPU)…")
    translator = HFSeq2SeqTranslator(model_id)
    print("✅  Listo — Ctrl+T traducir · Ctrl+L limpiar · Ctrl+Q salir\n")

    TranslateApp(translator).run()


if __name__ == "__main__":  # ejecución directa (python cli.py)
    main()
