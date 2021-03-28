# Procedimiento para correr el contenedor de Docker

La imagen de [Docker](https://www.docker.com/) está contenida en un repositorio público dentro de [DockerHub](https://hub.docker.com/) [lgarayv/pkg](https://hub.docker.com/r/lgarayv/pkg).

Para poder correr el contenedor es necesario descargar la imagen mediante un ```docker pull image```

```
docker pull lgarayv/pkg:0.1
```

![docker1](/images/docker1.png)

Posteriormente se crea el contenedor para poder correr el paquete. Es necesario tener habilitado el puerto 8888 ya que se comunica con este.


Para acceder a jupyter lab:

```
docker run --rm -it -p 8888:8888 lgarayv/pkg:0.1
```

![docker2](/images/docker2.png)

o 

Para acceder a jupyter lab referenciando una ruta local:

```
docker run --rm -v <ruta del directorio>:/datos --name jupyterlab_oa -p 8888:8888 -d lgarayv/pkg:0.1
```
![docker3](/images/docker3.png)

Nota: En el caso de windows es necesario cambiar los `/`por `\` en la ruta del directorio.

Posteriormente se dirige a la siguiente dirección y pedirá la contraseña `qwerty`.

http://localhost:8888/lab/tree/datos


![docker4](/images/docker4.png)

Una vez ingresada la contraseña se podrá trabajar con jupyter lab.

![docker5](/images/docker5.png)
Para acceder únicamente a la terminal:

```
docker exec -it jupyterlab_oa /bin/bash
```

Para salir de la terminal del contenedor se usa el comando ```exit```.


Para parar el contenedor:

```
docker stop jupyterlab_oa
```



