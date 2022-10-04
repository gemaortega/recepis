# Template Flask

## Instrucciones

1-. Clonar el repositorio y entrar en él.

**Importante:** Notar que dice `nombre_nuevo_proyecto` ese valor debe reemplazarse de los 
comandos de este cuadro. Recordar que esta carpeta quedará en el Escritorio (para eso es el `~/Desktop`).
```
git clone git@github.com:tristobal/template_flask.git ~/Desktop/nombre_nuevo_proyecto
cd ~/Desktop/nombre_nuevo_proyecto
```

2.- Eliminar la configuración previa de Git.
```
rm -rf .git
```

3.- Crear el entorno virtual y activarlo.
```
python -m venv venv
source venv/bin/activate
```

4.- Instalar dependencias (Flask, etc).
```
pip install -r requirements.txt
```

5.- Iniciar el servidor. Para detenerlo Ctrl (o Comando) + C.
```
python server.py
```


### Nota

A) Para inicializar Git.
```
git init
```


B) En caso de querer desactivar el entorno virtual, escribir en la terminal:
```
deactivate
```
