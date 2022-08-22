# GreenSoft

* Autor: Astra Team

* Prerequisitos:
    - Tener instalado Python 3 (Ultima version)
source .venv/bin/activate  //activate virtual env

* Como ejecutar la app local
    Prepara el ambiente en Windows (Ejecutar los siguientes comandos en BASH)
    py -m venv .venv  //Crear librerias
    source .venv/Scripts/activate  //actviar el ambiente virtual
    pip install -r requierements //Intalas las dependencias mencionadas ennrequierements.txt
    ************Servidor en Linea******

    NOTA: Contenido de ennrequierements.txt
                {
                pip install fastapi
                pip install "uvicorn[standard]"
                python -m pip install requests //instalar libreria de requests
                uvicorn main:app --reload //Correr la api mediente servidor local (localhost:8000)
                }

* Como probarla local mente
- Como abrirla cuando esta en ejecución