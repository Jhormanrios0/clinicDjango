# Proyecto IPS Salud y Vida

## Descripción del Proyecto

Este proyecto es un sistema de información desarrollado para la IPS "Salud y Vida" con el propósito de satisfacer las necesidades de almacenamiento de datos y garantizar la interoperabilidad de la historia clínica, conforme a la Resolución 866 del 2021 del Ministerio de Salud de la República de Colombia.

### Propósito de la Actividad

La finalidad de esta actividad es profundizar en el conocimiento y pensamiento analítico en diseño y desarrollo de algoritmos, aplicando estructuras de datos y Programación Orientada a Objetos (POO) para resolver problemas específicos en ingeniería de software.

## Módulos Desarrollados

1. **Módulo de Pacientes**

   - Permite la consulta, registro y actualización de los datos de los pacientes.
   - Incluye la estructura necesaria para manejar la información personal y médica de los pacientes de acuerdo con las regulaciones vigentes.

2. **Módulo de Contacto con el Servicio de Salud**
   - Incluye funcionalidades para consultar, crear y modificar registros de contacto con el servicio de salud.
   - Maneja diagnósticos utilizando el código CIE-10 en su versión más reciente, respetando la jerarquía de códigos de padres e hijos.

## Requisitos Específicos del Proyecto

El sistema ha sido desarrollado utilizando el framework **Django** y la base de datos **PostgreSQL**. A continuación, se detallan algunos requisitos específicos de los módulos de Pacientes y Contacto con el Servicio de Salud:

### 1. Información del Paciente

- **País de Nacionalidad**: Un paciente puede tener múltiples nacionalidades.
- **Fecha de Nacimiento**: Debe capturar tanto la fecha como la hora de nacimiento.
- **Ocupación**: Selección restringida a ocupaciones específicas según el estándar CIUO – 88 AC del DANE.
- **Oposición a la Presunción Legal de Donación** y **Documento de Voluntad Anticipada**: Deben estar estructurados de manera separada.
- **Categoría de Discapacidad**: Un paciente puede tener múltiples categorías de discapacidad.
- **Ciudad de Residencia**: Debe registrar el código de cada ciudad, conforme al sistema de códigos del DANE.

### 2. Contacto con el Servicio de Salud

- **Diagnóstico**: Representado con la versión más reciente del código CIE-10, utilizando una estructura jerárquica.

### 3. Reglas para Opciones de Campos

Para los campos que tienen opciones de selección, cada opción ha sido modelada como una entidad independiente en la base de datos, siempre que contenga más de 5 opciones.

### 4. Administración de Módulos

- **Panel de Control de Django**: Usado para gestionar estructuras de apoyo, como la de País.
- **Interfaz de Usuario**: Los demás módulos han sido diseñados para ser intuitivos y estéticamente agradables, utilizando **Tailwind CSS** para la estilización de las interfaces.

## Requisitos de Entrega

1. **Código Fuente**: Todo el código fuente del proyecto.
2. **Modelo Entidad-Relación**: Incluye el diseño de la base de datos en PostgreSQL, ubicado en la carpeta [documentation](documentation).

## Tecnologías Utilizadas

- **Backend**: Django, Python
- **Frontend**: Tailwind CSS, JavaScript
- **Base de Datos**: PostgreSQL

## Despliegue en Railway

Todo el proyecto ha sido desplegado en Railway y se puede acceder al panel de administración de Django en:

[https://clinicdjango.up.railway.app/admin/](https://clinicdjango.up.railway.app/admin/)

**Usuario**: `admin`  
**Contraseña**: `admin`

## Instalación

1. Clona el repositorio:
   ```bash
   git clone <https://github.com/Jhormanrios0/clinicDjango>
   ```
