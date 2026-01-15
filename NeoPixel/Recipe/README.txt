Indice
1. Proposito del codigo
2. Uso basico
3. Explicacion linea por linea

1. Proposito del codigo
Este programa en MicroPython permite leer y escribir un archivo de configuracion en formato clave=valor en la ruta absoluta /Recipe/recipe.txt. Sirve para guardar ajustes simples sin usar JSON ni librerias externas.

2. Uso basico
- Copia prgRecipe.py en el Raspberry Pi Pico (o en tu proyecto).
- Asegura que exista la carpeta /Recipe en la raiz del Pico.
- Para leer la configuracion:
    config = read_config_kv()
- Para actualizar o agregar un valor:
    config["NUEVO_PARAMETRO"] = "123"
- Para guardar la configuracion:
    write_config_kv(config)

3. Explicacion linea por linea
Linea 1: Define la funcion read_config_kv con la ruta por defecto /Recipe/recipe.txt.
Linea 2: Crea el diccionario vacio donde se guardaran las claves y valores.
Linea 3: Inicia un bloque try para capturar errores de apertura del archivo.
Linea 4: Abre el archivo en modo lectura.
Linea 5: Recorre el archivo linea por linea.
Linea 6: Elimina espacios y saltos de linea al inicio y al final.
Linea 7: Omite lineas vacias o que no contengan el caracter '='.
Linea 8: Continua al siguiente ciclo cuando la linea no es valida.
Linea 9: Separa la linea en clave y valor usando solo el primer '='.
Linea 10: Elimina espacios alrededor de la clave.
Linea 11: Elimina espacios alrededor del valor.
Linea 12: Verifica que la clave no este vacia.
Linea 13: Guarda la clave y el valor en el diccionario.
Linea 14: Captura el OSError cuando el archivo no existe o no se puede abrir.
Linea 15: Retorna un diccionario vacio si ocurre un error.
Linea 16: Retorna el diccionario con la configuracion cargada.
Linea 17: Linea en blanco para separar funciones.
Linea 18: Linea en blanco para separar funciones.
Linea 19: Define la funcion write_config_kv con la ruta por defecto /Recipe/recipe.txt.
Linea 20: Abre el archivo en modo escritura para sobrescribirlo.
Linea 21: Recorre cada par clave-valor del diccionario.
Linea 22: Escribe cada par en formato clave=valor y lo termina con un salto de linea.
