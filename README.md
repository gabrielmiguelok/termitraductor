# 📚 **TermiTraductor**

> Proyecto educativo y expositivo: demostrando cómo implementar un sistema autónomo y escalable de traducción local sin necesidad de APIs externas comerciales.

[![Licencia MIT](https://img.shields.io/badge/licencia-MIT-blue.svg)](LICENSE)
[![Python >=3.10](https://img.shields.io/badge/python-%3E%3D3.10-yellow)](https://python.org)
[![Repositorio GitHub](https://img.shields.io/badge/github-gabrielmiguelok-brightgreen)](https://github.com/gabrielmiguelok)

---

**TermiTraductor** es un proyecto pensado para mostrar cómo desarrollar un sistema escalable y autónomo de traducción, sin recurrir a APIs externas comerciales que puedan limitarse por cuotas o costos asociados, especialmente cuando se necesitan procesar cientos de miles de documentos.

La finalidad didáctica de este proyecto no es competir con herramientas populares como Google Translate, sino demostrar que es técnicamente posible y económicamente viable crear soluciones totalmente locales, evitando dependencias y costos recurrentes.

## 🎯 Objetivos Educativos

- ✅ Mostrar cómo automatizar traducciones de manera local usando modelos Seq2Seq.
- ✅ Enseñar la aplicación práctica de principios de diseño de software como SOLID, KISS y DRY.
- ✅ Proporcionar conocimiento sobre optimización y cuantización de modelos para su uso eficiente en recursos limitados.
- ✅ Inspirar desarrolladores para construir herramientas sostenibles, privadas y económicas.

## 🌟 ¿Por qué implementar un sistema local?

- **Costo-efectividad:** Traducción masiva sin costos incrementales.
- **Privacidad y seguridad:** Datos traducidos sin intermediarios ni terceros.
- **Escalabilidad total:** Sin restricciones por cantidad o volumen.
- **Autonomía tecnológica:** Soluciones independientes, sin riesgos comerciales.

## ✨ Características Clave

- 🔹 **Interfaz TUI** amigable basada en `prompt_toolkit`.
- 🔹 Uso de modelos preentrenados Seq2Seq desde [Hugging Face](https://huggingface.co).
- 🔹 Optimización mediante cuantización dinámica para eficiencia en CPU.
- 🔹 Atajos rápidos y accesibles para facilitar su uso en terminal.

## 📦 Instalación

Clona e instala localmente:

```bash
git clone https://github.com/gabrielmiguelok/termitraductor.git
cd termitraductor
pip install -e .
```

## 🚀 Ejecución Básica

Desde tu terminal:

```bash
termitraductor        # Inglés a español por defecto
termitraductor en-es  # Especificar idioma fuente y destino
```

En la interfaz TUI:

- Escribe el texto en el panel izquierdo.
- Usa **Ctrl + T** para traducir, **Ctrl + L** para limpiar, **Ctrl + Q** para salir.

## 🧩 Principios de Diseño Aplicados

`TermiTraductor` sirve como un claro ejemplo de:

- **KISS, DRY, YAGNI:** simplicidad y código sin redundancias.
- **SOLID:** estructuras limpias, responsabilidades definidas y fácil escalabilidad.
- **Composición sobre herencia:** flexibilidad en el desarrollo y expansión.

## 🗒️ Hoja de Ruta Educativa

- [x] Modelo optimizado en CPU con cuantización.
- [x] Interfaz TUI inicial y funcional.
- [ ] Casos prácticos de uso en traducción masiva.
- [ ] Tutoriales avanzados y documentación detallada.
- [ ] Soporte opcional GPU para grandes cargas de trabajo.

## 👨‍💻 Autor

Creado por [Gabriel Miguel](https://github.com/gabrielmiguelok)
**GitHub:** [https://github.com/gabrielmiguelok/TermiTraductor](https://github.com/gabrielmiguelok/TermiTraductor)

## 🌟 ¿Quieres contribuir?

Cualquier aporte educativo o práctico es bienvenido. Envía tus Pull Requests o Issues en [GitHub Issues](https://github.com/gabrielmiguelok/termitraductor/issues).

---
