from tkinter import Tk, filedialog


def constructor():

    colector = {
        "writer": "print",
        "key": "input",
        "extract": "import",
        "colect": "from",
        "conditional true": "if",
        "conditional false": "else",
        "conditional elif": "elif",
        "conditional &": "elif",
        "loop": "while",
        "class": "class",
        "function": "def",
        "<return>": "return",
        "alias": "as",
    }

    codigo = []
    indentacion = 0

    while True:
        entrada = input(">>: " * indentacion)

        # Eliminar los indicadores visuales escritos manualmente
        entrada = entrada.strip()

        while entrada.startswith(">>:"):
            entrada = entrada[3:].lstrip()

        # Finalizar la lectura del programa
        if entrada == "<end>":
            break

        # Cerrar un bloque
        if entrada == "<false>":
            if indentacion == 0:
                raise SyntaxError("No hay ningún bloque que cerrar")

            indentacion -= 1
            continue

        if entrada == "<save>":
            root = Tk()
            root.withdraw()

            ruta = filedialog.asksaveasfilename(
                title="Guardar archivo Candy",
                defaultextension=".cy",
                filetypes=[("Candy Files", "*.cy"), ("Todos los archivos", "*.*")],
                initialfile="programa.cy",
            )

            if ruta:
                with open(ruta, "w", encoding="utf-8") as archivo:
                    archivo.write("\n".join(codigo))

                print(f"Archivo guardado: {ruta}")
            else:
                print("Guardado cancelado.")

            root.destroy()

        # Ignorar líneas vacías
        if not entrada:
            continue

        # Traducir las palabras reservadas
        for nombre, funcion in colector.items():
            entrada = entrada.replace(nombre, funcion)

        # Generar la indentación real de Python
        codigo.append("    " * indentacion + entrada)

        # Abrir un bloque cuando termina en :
        if entrada.endswith(":"):
            indentacion += 1

    # Comprobar que todos los bloques estén cerrados
    if indentacion != 0:
        raise SyntaxError("Hay bloques sin cerrar con <false>")

    programa = "\n".join(codigo)

    exec(programa)


constructor()
