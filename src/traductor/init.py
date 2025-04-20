"""Paquete `traductor`.

Reexporta los puntos de entrada de alto nivel.
"""
from importlib.metadata import version as _v

from .cli import main

__all__ = ["main", "__version__"]
__version__: str = _v("traductor-tui")
