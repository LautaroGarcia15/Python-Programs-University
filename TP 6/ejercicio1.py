def eliminar_comentarios():
    try:
        arch_entrada = open("E:\\Programacion 1\\TP 6\\archej1.py","rt")
        arch_salida = open("SinComentarios.py", "wt")
        dentro_comillas_simples = False
        dentro_comillas_dobles = False
        docstring = False
        contenido = ""
        for linea in arch_entrada:
            for caracter in linea:
                if caracter == "'":
                    dentro_comillas_simples = not dentro_comillas_simples
                elif caracter == '"':
                    dentro_comillas_dobles = not dentro_comillas_dobles
                elif caracter == '#' and not dentro_comillas_simples and not dentro_comillas_dobles and not docstring:
                    break  # Ignorar el resto de la línea si se encuentra un '#' fuera de comillas o docstring
                contenido += caracter
            # Verificar si la línea contiene una cadena de documentación (docstring)
            if '"""' in linea:
                docstring = not docstring
        arch_salida.write(contenido)
    except FileNotFoundError:
        print("No se encontró el archivo.")
    except OSError as mensaje:
        print("ERROR: ", mensaje)

# Uso del programa
eliminar_comentarios()
