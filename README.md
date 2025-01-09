# Multi-Model Application

Este proyecto es una aplicación de Streamlit que permite a los usuarios interactuar con diferentes modelos de inteligencia artificial para tareas de generación de texto e identificación de imágenes. La aplicación está diseñada para ser fácil de usar y personalizar, permitiendo a los usuarios cambiar entre modelos y personalizar la interfaz visualmente.

## Características

- **Cambio de Modelos**: Cambia entre un modelo de generación de texto (`Qwen/Qwen2.5-0.5B-Instruct`) y un modelo de clasificación de imágenes (`google/vit-base-patch16-224`).
- **Interfaz Personalizable**: Selecciona iconos para representar preguntas y respuestas, mejorando la experiencia visual.
- **Generación de Texto**: Usa el modelo de texto para responder preguntas de manera interactiva.
- **Clasificación de Imágenes**: Sube imágenes para obtener clasificaciones automáticas.

## Requisitos

- Python 3.11 o superior
- [Streamlit](https://streamlit.io/)
- [Transformers](https://huggingface.co/transformers/)

## Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/tu_usuario/multi-model-app.git
   cd multi-model-app
   ```

2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## Uso

1. Ejecuta la aplicación de Streamlit:
   ```bash
   streamlit run multi_model_app/app.py
   ```

2. Abre tu navegador web y ve a `http://localhost:8501` para interactuar con la aplicación.

## Estructura del Proyecto

- `multi_model_app/app.py`: La aplicación principal que permite cambiar entre modelos y personalizar la interfaz.
- `multi_model_app/models.py`: Contiene la lógica para cargar y cambiar entre modelos.
- `qa_app/app.py`: Una aplicación secundaria para preguntas y respuestas usando el modelo de texto.
- `sentiment_analysis/app.py`: Una aplicación para análisis de sentimientos (no modificada en este proyecto).

## Personalización

- **Iconos**: Puedes seleccionar iconos para preguntas y respuestas desde la interfaz de usuario.
- **Modelos**: Cambia fácilmente entre los modelos de texto e imagen disponibles.

## Contribuciones

Las contribuciones son bienvenidas. Siéntete libre de abrir un issue o enviar un pull request.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.

## Contacto

Para preguntas o soporte, por favor contacta a [tu_email@ejemplo.com](mailto:tu_email@ejemplo.com). 
