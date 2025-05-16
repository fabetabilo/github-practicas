# git
    # Los git son versiones


# git init
    # Inicializa el repositorio git (.git) dentro del directorio en que se esta trabajando
    # por ejemplo, ejerciciosgit

# git status -s
    # Indica que pasa con este directorio y sus archivos: (??) -> no tiene "versonamiento"
    # (??): No tiene version, nada
    # (A): Archivo agregado 
    # (M): (ROJO) Archivo modificado no guardado
    # (M): (VERDE) Archivo modificado guardado

# git add .
    # (1) Agrega todo el directorio al versonamiento (.) pero tambien se puede agregar solo 1 archivo

# git commit -m "Mensaje cualquiera representativo"
    # (2) Realiza el commit 

# PRIMERA VEZ CON GIT:
#   git config --global user.email "you@example.com"    -- correo GitHub
#   git config --global user.name "Your Name"           -- usuario GitHub

# git log --oneline
    # Muestra el ID de la version del commit


print("UNO: Esta es la version uno")


print("DOS: Esta es la segunda version")

# Nota:
    # Tienes tu archivo, y lo modificas. Y verificas que el archivo se modifico (M roja):
        # git status -s

    # Para actualizar su version entonces:
        # git add .

    # Confirma que la modificacion se agrego (M verde):
        # git status -s

    # Haz el commit y confirma la nueva version:
        # git commit -m "Esta es la nueva version"

    # Luego, puedes confirmar y no aparecera nada en la cli
        # git status -s

    # Chequea las versiones con:
        # git log --oneline

            # b2339bd (HEAD -> master) Tercera : => Esta es la version actual
            # cee0b06 Segunda version
            # 94479e5 Primera version

    # Navega y "regresa" a traves de las versiones con:
        # git reset --hard [ID_VERSION]

        # EJEMPLO:
            # git reset --hard 94479e5 (Vuelve a la Primer Version)

    # Termina, y envialo a Remote
        # git push

print("SEIS: Este es el final en GitHub")

    # git add .
    # git commit -m "Seis"
    # git log --oneline
        # -- muestra un origin/main
    # git push
