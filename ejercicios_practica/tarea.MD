![Inove banner](inove.jpg)
Inove Escuela de Código\
info@inove.com.ar\
Web: [Inove](http://inove.com.ar)

---
# Tarea: Django - Templates

Al realizar esta tarea pondremos en práctica los conocimientos adquiridos en clase.
Una vez finalizada, el alumno debe subir el enlace a su repositorio "forkeado" el foro de tarea correspondiente -NO SE ADMITE LA DEVOLUCIÓN POR OTRO CANAL SALVO SE ESPECIFIQUE LO CONTRARIO- 

Recuerde que no debe subir la base de datos al sistema, para ello se encuentra el archivo .gitignore que especifica los archivos y directorios omitidos.

---

### 1. Establecer configuraciones para el trabajo con los templates y archivos estáticos.
A partir de lo visto en clase y de la documentación de Django Templates, realice las modificaciones necesarias en el archivo settings.py para poder trabajar con archivos estáticos y templates, así mismo, debe crear las carpetas necesarias y ordenar las existentes.

### 2. Collectstatic
Ejecute el comando:

```
python manage.py collectstatic
```
... (dentro del contenedor) para recolectar los archivos estáticos del proyecto y probar que la configuración del punto 1 sea correcta.

### 3. Desarrolle 5 templates HTML.
Desarrolle 5 archivos html, con los nombres que usted decida, colóquelos en el directorio "Templates".
Estos archivos deben tener:

* 1 Tabla HTML.
* 1 Lista HTML.
* 1 Formulario HTML.
* Texto en todas las etiquetas vistas en clase (h1 a h6 y p).
* 1 Imagen que sirva de enlace a una url.

Cada página debe tener al menos una de estas etiquetas.
El atributo "action" del formulario puede estár vacío (""), el objetivo es ver cómo se renderiza cada template html.

### 4. Desarrolle las vistas para dichos templates.
Realice las vistas basadas en la clase TemplateView para poder renderizar cada uno de estos templates creados en el punto 3.

### 5. Genere un archivo urls.py para la aplicación "e_commerce"
Debe generar un archivo urls.py para la aplicación "e_commerce" (no confundir con las urls de las APIs) y vincularlo a las urls generales.

Luego, genere las urls para las vistas desarrolladas en el punto 4.

### 6. Desarrolle un formulario para insertar un comic en la base de datos.
Desarrolle un formulario para insertar un comic en la base de datos. 
Recomendamos:
Utilizar los "type" de los inputs con los atributos:
* number  
* text  
* url  
Para los campos que correspondan al modelo "Comic"

> **IMPORTANTE**: Debe utilizar la etiqueta **{%csrf_token%}** dentro del formulario, será explicada en clases posteriores.
Para ello, debe incluirla dentro de la etiqueta "form", por ejemplo:

```
<form action="destino" method="POST">{%csrf_token%}
...
...
</form>
```

Aproveche las APIs creadas para darle el destino a este formulario e insertar el registro a la base de datos.

---

## ¿Dudas?
Ante cualquier inquietud, debe referirse a los canales especificados para su trato en inove.