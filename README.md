# Laboratorio Testing

## Requisitos previos

- Tener instalado **Python 3** en tu sistema.

## Configuración del entorno

1. **Crear un entorno virtual**

   Abre una terminal en la raíz del proyecto y ejecuta:

   ```sh
   python3 -m venv env
   ```

2. **Activar el entorno virtual**

   - En macOS/Linux:
     ```sh
     source env/bin/activate
     ```
   - En Windows:
     ```sh
     .\env\Scripts\activate
     ```

3. **Instalar las dependencias**

   Ejecuta el siguiente comando para instalar las dependencias necesarias:

   ```sh
   pip install -r requirements.txt
   ```

## Ejecutar pruebas

Para correr las pruebas, usa:

```sh
python -m pytest
```
