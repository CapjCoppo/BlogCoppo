# Instrucciones de cómo agregar contenido al Blog

Este archivo tiene como finalidad dar la información necesaria para poder agregar contenido al blog. Información de cómo modificar aspectos de la página web y los sistemas necesarios para poder ejecutarlo de manera local antes de subirlo a la página.

## Requisitos de sistema
Idealmente el sistema operativo más idóneo sería Linux. Sin embargo con windows también se puede. 
Todas las instrucciones se ven relacionadas con Linux.

* Python  3.9.X
* Git 2.30.X
* Pelican 4.8.X

Esto sería lo esencial, sin embargo existe el archivo ***requeriments.txt*** en donde encontrara todas las dependencias que hasta la fecha se han utilizado para generar este blog.

> Una forma de instalar todas las dependencias sería con el siguiente commando 
>~~~
>$ pip3 install -r requirements.txt
>~~~

## También es necesario installar Pelican

Para instalar hay que ejecutar el siguiente comando en la terminal
~~~
python -m pip install "pelican[markdown]"
~~~
## Descarga de repositorio
Para descargar el repositorio lo haremos via terminal.

1. En el caso que deba ser descargada por la terminal de linux sería
`$git clone https://github.com/CapjCoppo/BlogCoppo.git`

2. Descargar el submodulo que el tema
`git submodule update --init --recursive`

## Programas necesarios
Los programas necesarios seria un editor de código como podría ser *Visual Studio Code* o similares. *Git* para el manejo de versiones y *Python* para que podamos generar todo lo necesario.

## Cómo agregar un post
Para agregar un post es necesario crear el archivo en la ruta `\content` acá se debe generar un archivo con el nombre del post el cual debe ser distinto al de todos los archivos y en extensión **.md**.

La ***metadata*** necesaria para crear un post es la siguiente:
~~~
Title: El titulo del post
Date: 2023-10-23 15:53
Category: Linux
Authors: Carlos Carrasco Varas
Summary: Acá va el resumen del artículo que es el que se visualizara en el blog.

# Titulo del blog
...

~~~
Una vez realizado este proceso se debe guardar el documento y ejecutar los scripts que se indican a continuación.
## Comandos necesarios para correr el programa
Para generar el sitio web estático es necesario correr los siguientes comando en el orden indicado:

~~~
$ make clean
$ make html
$ pelican -r -l
~~~

Si queremos comprobar que todo esta en orden este último comando `$ pelican -r -l` producirá un servidor local viendo todos los cambios que hemos realizado.

Ejecutando este código en la terminal estaríamos en condiciones de pushear la página a nuestra rama **master**.
~~~
$ git status
$ git add .
$ git status
$ git commit -m ":memo: Se actualiza blog"
$ git push -u origin master 
~~~
> Recuerde que debe tener habilitada su llave SSH para hacerlo de esta manera. En caso que no tenga llave con **Github Desktop** también se produce el mismo resultado.
