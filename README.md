# Chatbot de Atención a Pacientes para Centros de Salud de Argentina

## Descripción

Este proyecto tiene como objetivo desarrollar un chatbot que brinde asistencia a pacientes en centros de salud de Argentina, utilizando la versión 3.1 del framework Rasa. El chatbot utiliza respuestas preestablecidas para guiar a los pacientes en diversas consultas y tareas relacionadas con su salud.

## Características principales

* **Respuestas preestablecidas:** El chatbot ofrece respuestas informativas y útiles a preguntas frecuentes de los pacientes, como solicitud y modificación de turnos, consultas sobre horarios de atención, medios de pago, o ubicación de servicios, etc.
* **Fácil de usar:** La interfaz del chatbot es intuitiva y fácil de navegar, lo que permite a los pacientes obtener la información que necesitan de manera rápida y sencilla.
* **Asistencia en horario de atención:** El chatbot está diseñado para brindar asistencia a los pacientes durante el horario de atención al público del centro de salud. ¿Cómo funciona?
    * **a. Recopilación de información:** El chatbot recopilará los datos del paciente y el motivo de su consulta de manera eficiente.
    * **b. Transferencia a personal humano:** Una vez recopilada la información necesaria, el chatbot transferirá la consulta a un miembro del personal del centro de salud para que brinde atención personalizada.
* **Personalizable:** El chatbot puede ser adaptado a las necesidades específicas de cada centro de salud, incluyendo información y recursos relevantes para su comunidad.

## Tecnologías utilizadas

* **Python:** Lenguaje de programación principal para el desarrollo del chatbot.
* **Rasa:** Framework de código abierto para la creación de chatbots conversacionales.

## Instalación

**Requisitos previos:**

* **Git:** Asegurate de tener Git instalado en tu sistema. Podés descargarlo e instalarlo desde [https://git-scm.com/](https://git-scm.com/).
* **Python 3.x:** Necesitarás tener Python 3.x instalado. Podés verificar la versión que tenés con el comando `python3 --version` en tu terminal. Si no lo tenés, podés descargarlo desde [https://www.python.org/](https://www.python.org/).

**Pasos:**

1. **Clonar el repositorio:**

   * Abrí tu terminal o línea de comandos.
   * Navegá a la carpeta donde deseás guardar el proyecto.
   * Ejecutá el siguiente comando para clonar el repositorio:

     ```bash
     git clone [https://github.com/tu_usuario/tu_repositorio.git](https://github.com/tu_usuario/tu_repositorio.git)
     ```

   * Reemplazá `tu_usuario` con tu nombre de usuario de GitHub y `tu_repositorio` con el nombre de tu repositorio.

2. **Crear un entorno virtual (recomendado):**

   * Un entorno virtual te permitirá aislar las dependencias de tu proyecto.
   * Navegá a la carpeta del proyecto que acabás de clonar:

     ```bash
     cd tu_repositorio
     ```

   * Creá un entorno virtual llamado `venv`:

     ```bash
     python3 -m venv venv 
     ```

   * Activá el entorno virtual:

     * En sistemas Unix/Linux:

       ```bash
       source venv/bin/activate
       ```

     * En Windows:

       ```bash
       venv\Scripts\activate
       ```

3. **Instalar las dependencias:**

   * Con el entorno virtual activado, instalá las librerías necesarias para el proyecto, incluyendo Rasa 3.1:

     ```bash
     pip install -r requirements.txt
     ```

4. **Entrenar y ejecutar el chatbot:**

   * Finalmente, entrená y ejecutá el chatbot con los siguientes comandos:

    ```bash
     rasa train 
     ```
    
     ```bash
     rasa run actions & rasa shell 
     ```

   * Esto abrirá una interfaz de chat en tu terminal donde podrás interactuar con el chatbot utilizando el modelo pre-entrenado.

**¡Listo!** Ahora podés utilizar el chatbot en tu propia computadora.


## Contribuciones

¡Las contribuciones son bienvenidas! Si deseas mejorar este proyecto, puedes:

* Informar sobre errores o problemas.
* Sugerir nuevas características o mejoras.
* Enviar pull requests con tus cambios.

## Licencia

Este proyecto está bajo la licencia Apache 2.0 (Open Source).

## Contacto

Si tenés alguna pregunta o comentario, no dudes en contactarme a través de tamaramaggioni@gmail.com