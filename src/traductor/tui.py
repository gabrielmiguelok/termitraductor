"""Interfaz TUI basada en prompt_toolkit (SoC: interfaz ≠ negocio)."""

from __future__ import annotations

import asyncio
from typing import Final

from prompt_toolkit import Application
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.layout import HSplit, Layout, VSplit, Window
from prompt_toolkit.layout.controls import FormattedTextControl
from prompt_toolkit.styles import Style
from prompt_toolkit.widgets import Box, Button, Frame, TextArea

from .dto import TranslationRequest, TranslationResponse
from .translator import Translator

__all__ = ["TranslateApp"]

_STATUS_TEXT: Final[str] = "Ctrl+T traducir │ Ctrl+L limpiar │ Ctrl+Q salir"


class TranslateApp:
    """Capa de presentación: maneja eventos y actualiza la vista."""

    def __init__(self, translator: Translator) -> None:
        self._translator = translator
        self._build_ui()

    # --------------------------------------------------------------------- #
    #  Construcción de la interfaz (privado)                                #
    # --------------------------------------------------------------------- #
    def _build_ui(self) -> None:
        self._input_area = TextArea(prompt="> ", scrollbar=True)
        self._output_area = TextArea(
            scrollbar=True,
            read_only=True,
            style="class:output",
        )

        # ----------------------  Botones  ---------------------------------
        translate_btn = Button("Traducir", handler=self._on_translate)
        clear_btn = Button("Limpiar", handler=self._on_clear)
        quit_btn = Button("Salir", handler=lambda: self._app.exit())

        buttons_row = Box(
            body=VSplit([translate_btn, clear_btn, quit_btn], padding=3, align="CENTER"),
            height=3,
            style="class:button-bar",
        )

        # --------------------  Key Bindings  ------------------------------
        kb = KeyBindings()

        @kb.add("c-t")
        def _kb_translate(event) -> None:  # noqa: D401
            asyncio.create_task(self._translate())

        @kb.add("c-l")
        def _kb_clear(event) -> None:  # noqa: D401
            self._on_clear()

        @kb.add("c-q")
        def _kb_quit(event) -> None:  # noqa: D401
            event.app.exit()

        # -----------------------  Layout  ---------------------------------
        body = VSplit(
            [
                Frame(self._input_area, title="Fuente"),
                Frame(self._output_area, title="Traducción"),
            ],
            padding=1,
            padding_char="│",
        )

        root = HSplit(
            [
                body,
                buttons_row,
                Window(
                    content=FormattedTextControl(_STATUS_TEXT),
                    height=1,
                    style="class:status",
                ),
            ]
        )

        self._app = Application(
            layout=Layout(root, focused_element=self._input_area),
            key_bindings=kb,
            full_screen=True,
            style=_theme(),
        )

    # --------------------------------------------------------------------- #
    #  Event‑handlers                                                       #
    # --------------------------------------------------------------------- #
    def _on_translate(self) -> None:
        asyncio.create_task(self._translate())

    def _on_clear(self) -> None:
        self._input_area.text = ""
        self._output_area.text = ""

    # --------------------------------------------------------------------- #
    #  Lógica asíncrona (mantiene la UI reactiva)                           #
    # --------------------------------------------------------------------- #
    async def _translate(self) -> None:
        src_text = self._input_area.text.strip()
        if not src_text:
            return  # Nada que hacer

        loop = asyncio.get_running_loop()
        req = TranslationRequest(src_text.splitlines())
        resp: TranslationResponse = await loop.run_in_executor(
            None, self._translator.translate, req
        )
        self._output_area.text = "\n".join(resp.translated)

    # --------------------------------------------------------------------- #
    #  API pública                                                          #
    # --------------------------------------------------------------------- #
    def run(self) -> None:
        """Arranca la aplicación en modo pantalla completa."""
        self._app.run()


def _theme() -> Style:
    """Paleta de colores centralizada (Futuros temas = Open/Closed)."""
    return Style.from_dict(
        {
            "output": "bg:#1e1e1e #e8e8e8",
            "status": "bg:#444444 #ffffff",
            "button-bar": "bg:#222222",
        }
    )
