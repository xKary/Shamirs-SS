# Shamir Secret Sharing
- Alcántara Valdés José Angel
- Del Río Pulido Erik Federico
- Prado Oropeza Karina Vianey

### Descripción
Programa que implementA el esquema de Shamir para compartir la clave necesaria para descifrar un archivo. Dicha información debe poder ser accedida siempre que estén presentes, al menos T, de los n miembros de un grupo de personas con autorización para acceder a ella.

### Requerimientos previos

  - Tener [Python](https://www.python.org/downloads/) 3 o una versión superior.
  - Tener los siguientes módulos:
     - [gmpy2](https://pypi.org/project/gmpy2/2.1.0a2/)
     - [pycryptodome](https://pypi.org/project/pycryptodome/)

### Usar el programa
  - Descargar el la carpera Shamirs-SS en su ordenador.
  - Abrir la terminal y acceder a dicha carpeta.
    Linux
     ```sh
        $ cd Shamirs-SS
      ```
   - Para utilizar el programa utilice el siguiente comando.
        ```sh
            $ python main.py
        ```
 - El programa iniciará su ejecución, le mostrará un menú de opciones y le pedirá la información necesaria para realizar la accion seleccionada.
### Tests
Todo los módulos del programa cuentan con pruebas unitarias, para ejecutarlar ejecutar el siguiente comando:
  - Compilar el test.
    ```sh
        $ python -m unittest -v
    ```
 ### Documentación
 La documentación del programa se encuentra en la carpeta docs, para visualizarla abrir la página *docs/api/index.html* en el navegador de su preferencia.
