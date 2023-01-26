Title: Segundo Post
Date: 2023-01-26 15:32
Category: principal, otros
Slug: hola-mundo
Authors: Rafnix Guzmán
Tags: Informatica, Linux, Pruebas
Summary: en esta se ve como crear una página


# Como agregar contenido al repositorio

1. Crear una carpeta en documentos
2. Abrir Carpeta con **Visual Studio Code** o editor favorito
3. Abrir terminal y escribir lo siguiente `git clone --recurse-submodules git@github.com:CapjCoppo/BlogCoppo.git`
4. Esto nos solicitará nuestras llaves SSH que ya deberíamos tener agregadas en nuestra cuenta github
5. Esperar que el proceso de descarga finalice y podemos agregar el nuevo artículo
 
# Generar la página
```
make clean
make html
make publish
```

# agreando una foto

![Carlos](images/Pic-1.jpeg)
