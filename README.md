# IT2 Planificación y Gestión de Infraestructuras TIC

## Autores

-   Luis Javier Horcajada Torres - [LuisJavier.Horcajada\@alu.uclm.es](mailto:LuisJavier.Horcajada@alu.uclm.es)

## Objetivo del proyecto

El Objetivo del trabajo es desplegar la arquitectura TIG en diversos nodos virtualizados con *Vagrant* y automatizados con *Ansible*, para ello se plantea esta solución:

-  **Broker MQTT**: Este es el que obtendrá los datos y se los enviará a telegraf, este nodo se despliega en **AWS**.
-  **Telegraf**: Es el agente que recolecta los datos y los envía a InfluxDB, se despliega en una VM en local.
-  **InfluxDB**: Es la base de datos, se despliega en una VM en local.
-  **Grafana**: Es una herramienta que se conecta a InfluxDB y permite visualizar los datos, se despliega en una VM en local.

## Estructura

Se va a describir la estructura de los archivos:

### Files

En esta carpeta se encuentran los siguientes archivos:

-  **pgi1.pem**: La clave privada para el nodo de AWS. *Se debe modificar con la clave del nodo*.
-  **broker.conf**: Configuración para el broker de MQTT para el nodo 1.
-  **telegraf.conf**: Configuración de Telegraf con MQTT.
-  **datasource.yaml**: Incluye el datasource con InfluxDB para poder visualizar los datos en Grafana.
-  **dashboard.json**: Incluye un dashboard de ejemplo.
-  **dashboard.yaml**: Incluye la configuración básica del dashboard.



### Directorio principal

-  **playbook.yml**: Contiene los pasos que Ansible ejecutará para preparar el entorno en cada nodo e instalar las herramientas y ejecutar el flujo de datos.
-  **Vagrantfile**: Despliega los nodos de las máquinas virtuales locales.
-  **hosts**: Contiene la configuración y datos necesarios para ansible.
-  **mqtt_publish.py**: Configuración para enviar datos mediante MQTT al broker en el nodo de AWS.

## Dependencias

### Ansible

`sudo apt install ansible`

### Vagrant

`sudo apt install virtualbox virtualbox-dkms vagrant`

### Python3

`sudo apt install python3`

## Ejecución

Aquí se va a explicar como ejecutar correctamente el proyecto, teniendo en cuenta que no se explicará como desplegar el nodo en AWS.

### Desplegar los nodos locales

`vagrant up`

### **(Opcional)** Comprobar la conectividad de los nodos

Es necesario tener en cuenta que posiblemente la autenticación de los nodos falle ya que se debe limpiar el contenido del fichero *~/.ssh/known_hosts*.

`ansible -i hosts all -m ping`

### Lanzar el playbook

`ansible-playbook -i hosts playbook.yml`

### Ejecutar el publisher de MQTT

`python3 mqtt_publish.py`

### Acceder a Grafana

Insertar en cualquier browser *localhost:8080* y acceder al dashboard para ver los datos.

- usuario: admin
- password: admin

## Consideraciones Adicionales

- Las máquinas virtuales locales utilizan CentOs 7, puede que con otras distribuciones no funcione.
- Se debe incluir la clave privada del nodo en aws en el archivo pgi1.com y poner los permisos de este archivo a solo lectura mediante `chmod 0400 files/pgi1.pem`.
- Se debe modificar el archivo **hosts** con la IP correspondiente del nodo en AWS en el node1 ansible_ssh_host.
- Se debe modificar el archivo **mqtt_publish.py** y cambiar el broker con la IP correspondiente del nodo en AWS.
- Se debe modificar el archivo **telegraf.conf** y cambiar la IP de servers con la IP correspondiente del nodo en AWS.
