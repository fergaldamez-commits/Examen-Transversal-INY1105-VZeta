# Examen-Transversal-INY1105-VZeta



\# Evaluación Final Transversal - Caso VZeta



\*\*Estudiante:\*\* Fernando Galdamez  

\*\*Usuario GitHub:\*\* fergaldamez-commits  

\*\*Asignatura:\*\* Infraestructura de Aplicaciones I (INY1105)  

\*\*Institución:\*\* Duoc UC



\---



\## 1. Justificación Técnica



\### Contenedores vs. Hipervisores (On-Premise)

Para la modernización de los despliegues de VZeta, se propone la utilización de \*\*contenedores (Docker)\*\* en lugar de máquinas virtuales tradicionales (hipervisores) por las siguientes razones clave:

\* \*\*Eficiencia de Recursos y Arquitectura:\*\* A diferencia de los hipervisores (como VMware o Hyper-V) que requieren virtualizar todo el hardware e instalar un Sistema Operativo (Guest OS) completo para cada aplicación, los contenedores comparten el kernel del host. Esto los hace significativamente más ligeros, permitiendo empaquetar la aplicación y sus dependencias sin el sobrecosto de un SO adicional.

\* \*\*Tiempos de Despliegue:\*\* Un contenedor se inicia en cuestión de segundos, mientras que una máquina virtual on-premise requiere el proceso completo de booteo del sistema operativo.

\* \*\*Licenciamiento y Costos:\*\* La virtualización tradicional on-premise suele conllevar altos costos en licencias de software (tanto del hipervisor como de los sistemas operativos invitados, ej. Windows Server). Docker Engine, por otro lado, es de código abierto (Open Source), eliminando los costos de licenciamiento de software y maximizando el retorno de inversión (ROI).



\### Propuesta de Entorno Cloud

\* \*\*Nube Pública, Privada e Híbrida:\*\* Una nube privada on-premise brindaría control total, pero exigiría un alto capital inicial para hardware y mantenimiento. Una nube híbrida aportaría flexibilidad, pero sumaría complejidad a la gestión actual de VZeta. Por lo tanto, se justifica el uso de una \*\*Nube Pública (AWS)\*\* bajo el modelo IaaS (Instancias EC2). 

\* \*\*Elección Tecnológica:\*\* Dado que la infraestructura actual de VZeta no soporta orquestadores avanzados como Kubernetes (K8s) o servicios gestionados (EKS), la solución óptima es utilizar \*\*Docker Compose\*\* a nivel de host sobre una instancia Amazon EC2. Esto permite agilidad, escalabilidad bajo demanda, facturación por uso y una orquestación centralizada de los microservicios sin la complejidad de un clúster.



\---



\## 2. Descripción de la Arquitectura



La solución está basada en una arquitectura de microservicios contenerizados, orquestados mediante `docker-compose`. Consta de tres servicios principales que se comunican a través de una red interna tipo Bridge (`vzeta\_network`):



1\. \*\*mynginx\_container (NGINX):\*\* Actúa como \*Reverse Proxy\*. Es el único punto expuesto a internet (escucha en el puerto 80 del host) y redirige el tráfico HTTP interno hacia la aplicación web.

2\. \*\*myapp\_container (Aplicación Flask):\*\* Aplicación web desarrollada en Python. Su imagen fue construida de forma personalizada mediante un `Dockerfile` (partiendo de `python:3-slim`). Contiene la lógica para conectarse a la base de datos y mostrar el contador de visitas.

3\. \*\*db\_container (PostgreSQL):\*\* Base de datos relacional (imagen oficial de PostgreSQL 13). Almacena el registro de visitas. Utiliza un volumen local (`db\_data`) montado en `/var/lib/postgresql/data` para garantizar la \*\*persistencia de los datos\*\* incluso si el contenedor es destruido o reiniciado.



\---



\## 3. Procedimiento de Despliegue (Paso a Paso)



Para levantar esta infraestructura desde cero en el servidor host (Amazon EC2 con Docker y Docker Compose instalados), se deben ejecutar los siguientes comandos:



1\. \*\*Clonar el repositorio y acceder a la carpeta:\*\*

&#x20;  ```bash

&#x20;  git clone \[https://github.com/fergaldamez-commits/Examen-Transversal-INY1105-VZeta.git](https://github.com/fergaldamez-commits/Examen-Transversal-INY1105-VZeta.git)

&#x20;  cd repo

