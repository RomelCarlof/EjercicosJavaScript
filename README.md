# EjercicosJavaScript
ejercicios

# 1. solo cuando no se configuro
git remote add backendFullstack  https://github.com/RomelCarlof/EjercicosJavaScript.git

# 2. Luego verifica que se agregó correctamente con:

git remote -v

# 3.  prueba hacer el fetchcon el nuevo nombre:

git fetch backendFullstack

# 4.  Para fucionar y guardar (Mayúsculas + Z dos veces)
SHIFT + ZZ  

# Si prefieres reescribir el historial y aplicar los cambios de backendFullstack/main encima de main, usa:
git checkout main
git rebase backendFullstack/main




# 5.  rn caso no funcione la fusión seguir los siguientes pasos 
git status
git commit
git commit -m "Finalizando merge"
git push origin main
git push origin main
git status

# 5. Cambiar a la rama en la que quieres fusionar
git checkout main


/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Si quieres cambiar a esa rama (si aún no lo has hecho), usa:

git checkout main

 # si aún no la tienes localmente, crea la rama y sigue la remota con:

git checkout -b main backendFullstack/main


# Si necesitas actualizar los cambios desde el remoto, usa:

git pull backendFullstack main
git pull origin main







//¿Qué debes hacer?
✅ Si el código lo escribiste tú o confías en la fuente (por ejemplo, en este caso que lo hicimos juntos), puedes:

Escribir en la consola.
allow pasting 

Presionar Enter.

Luego pegar tu código.