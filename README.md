## Parte 2 para la práctica 1 del curso de Optimización 2 2021-1: implementación de método numérico para resolver problemas de optimización convexa.

* Data set: por definir

**Profesor**: Erick Palacios Moreno

**Equipo 5.**
______

| Github User  | Actividad a realizar                                                       |
|:------------:|:--------------------------------------------------------------------------:|
| @carlosrlpzi | 1. Programar el método numérico y seleccionar los ejemplos para los tests. |
| @lobolc      | 1. Programar el método numérico y seleccionar los ejemplos para los tests. |
| @lgarayva    | 2. Construir github workflows (build & push y tests) y documentar paquete. |
| @ZarCorvus   | 3. _Project Manager_. Búsqueda de ejemplos y documentación para las tareas. Crear botón de binder. Publicar documentación del paquete online. |

______

Para una experiencia interactiva con el código de nuestro repositorio, puedes utilizar el botón [binder](https://mybinder.org/):

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/optimizacion-2-2021-1-gh-classroom/practica-1-segunda-parte-jlrzarcor.git/main)

______

Puedes visitar nuestro sitio para conocer la documentación del paquete en línea:

[opt_grad_desc](https://optimizacion-2-2021-1-gh-classroom.github.io/practica-1-segunda-parte-jlrzarcor/)
______

** Estructura de la información:**
* Por definir

______
**Referencias:**

* Por definir



### Estructura de carpetas

```
.
├── README.md
├── dockerfiles
│   ├── README.md
│   └── pkg
│       └── Dockerfile
├── docs
│   └── sphinx_doc
│       ├── Makefile
│       ├── _build
│       │   ├── doctrees
│       │   │   ├── contact.doctree
│       │   │   ├── help.doctree
│       │   │   ├── index.doctree
│       │   │   ├── license.doctree
│       │   │   ├── log_reg.doctree
│       │   │   └── modules.doctree
│       │   └── html
│       │       ├── _sources
│       │       │   ├── contact.rst.txt
│       │       │   ├── crash_pai.rst.txt
│       │       │   ├── ejemplo.rst.txt
│       │       │   ├── help.rst.txt
│       │       │   ├── index.rst.txt
│       │       │   ├── license.rst.txt
│       │       │   ├── log_reg.rst.txt
│       │       │   ├── modules.rst.txt
│       │       │   ├── simple_fire.rst.txt
│       │       │   ├── test.rst.txt
│       │       │   └── test_sample1.rst.txt
│       │       ├── _static
│       │       │   ├── alabaster.css
│       │       │   ├── basic.css
│       │       │   ├── css
│       │       │   │   ├── badge_only.css
│       │       │   │   ├── fonts
│       │       │   │   │   ├── Roboto-Slab-Bold.woff
│       │       │   │   │   ├── Roboto-Slab-Bold.woff2
│       │       │   │   │   ├── Roboto-Slab-Regular.woff
│       │       │   │   │   ├── Roboto-Slab-Regular.woff2
│       │       │   │   │   ├── fontawesome-webfont.eot
│       │       │   │   │   ├── fontawesome-webfont.svg
│       │       │   │   │   ├── fontawesome-webfont.ttf
│       │       │   │   │   ├── fontawesome-webfont.woff
│       │       │   │   │   ├── fontawesome-webfont.woff2
│       │       │   │   │   ├── lato-bold-italic.woff
│       │       │   │   │   ├── lato-bold-italic.woff2
│       │       │   │   │   ├── lato-bold.woff
│       │       │   │   │   ├── lato-bold.woff2
│       │       │   │   │   ├── lato-normal-italic.woff
│       │       │   │   │   ├── lato-normal-italic.woff2
│       │       │   │   │   ├── lato-normal.woff
│       │       │   │   │   └── lato-normal.woff2
│       │       │   │   └── theme.css
│       │       │   ├── custom.css
│       │       │   ├── doctools.js
│       │       │   ├── documentation_options.js
│       │       │   ├── file.png
│       │       │   ├── jquery-3.5.1.js
│       │       │   ├── jquery.js
│       │       │   ├── js
│       │       │   │   ├── badge_only.js
│       │       │   │   ├── html5shiv-printshiv.min.js
│       │       │   │   ├── html5shiv.min.js
│       │       │   │   └── theme.js
│       │       │   ├── language_data.js
│       │       │   ├── minus.png
│       │       │   ├── plus.png
│       │       │   ├── pygments.css
│       │       │   ├── searchtools.js
│       │       │   ├── underscore-1.12.0.js
│       │       │   └── underscore.js
│       │       ├── contact.html
│       │       ├── genindex.html
│       │       ├── help.html
│       │       ├── index.html
│       │       ├── license.html
│       │       ├── log_reg.html
│       │       ├── modules.html
│       │       ├── objects.inv
│       │       ├── search.html
│       │       ├── searchindex.js
│       │       └── test.html
│       ├── conf.py
│       ├── contact.rst
│       ├── help.rst
│       ├── index.rst
│       ├── license.rst
│       ├── log_reg.rst
│       ├── make.bat
│       └── modules.rst
├── images
│   ├── aws_workscreen_1.jpg
│   ├── aws_workscreen_2.jpg
│   ├── docker1.png
│   ├── docker2.png
│   ├── docker3.png
│   ├── docker4.png
│   └── docker5.png
├── instrucciones.ipynb
├── notebooks
│   ├── GDA.ipynb
│   ├── LR_test.ipynb
│   ├── datasets
│   │   └── breast_cancer_wisconsin_(original)_dataset.txt
│   └── reg_log_doc.ipynb
├── oa_e5
│   ├── __init__.py
│   └── __pycache__
│       └── __init__.cpython-37.pyc
├── old_README.md
├── references
│   └── Documentation
│       └── Uryasev-AlgorithmsOptimizationCVaR.pdf
├── requirements.txt
├── src
│   ├── docs
│   │   └── sphinx_doc
│   │       ├── Makefile
│   │       ├── _build
│   │       │   ├── doctrees
│   │       │   │   ├── contact.doctree
│   │       │   │   ├── help.doctree
│   │       │   │   ├── index.doctree
│   │       │   │   ├── license.doctree
│   │       │   │   ├── log_reg.doctree
│   │       │   │   └── modules.doctree
│   │       │   └── html
│   │       │       ├── _sources
│   │       │       │   ├── contact.rst.txt
│   │       │       │   ├── crash_pai.rst.txt
│   │       │       │   ├── ejemplo.rst.txt
│   │       │       │   ├── help.rst.txt
│   │       │       │   ├── index.rst.txt
│   │       │       │   ├── license.rst.txt
│   │       │       │   ├── log_reg.rst.txt
│   │       │       │   ├── modules.rst.txt
│   │       │       │   ├── simple_fire.rst.txt
│   │       │       │   ├── test.rst.txt
│   │       │       │   └── test_sample1.rst.txt
│   │       │       ├── _static
│   │       │       │   ├── alabaster.css
│   │       │       │   ├── basic.css
│   │       │       │   ├── css
│   │       │       │   │   ├── badge_only.css
│   │       │       │   │   ├── fonts
│   │       │       │   │   │   ├── Roboto-Slab-Bold.woff
│   │       │       │   │   │   ├── Roboto-Slab-Bold.woff2
│   │       │       │   │   │   ├── Roboto-Slab-Regular.woff
│   │       │       │   │   │   ├── Roboto-Slab-Regular.woff2
│   │       │       │   │   │   ├── fontawesome-webfont.eot
│   │       │       │   │   │   ├── fontawesome-webfont.svg
│   │       │       │   │   │   ├── fontawesome-webfont.ttf
│   │       │       │   │   │   ├── fontawesome-webfont.woff
│   │       │       │   │   │   ├── fontawesome-webfont.woff2
│   │       │       │   │   │   ├── lato-bold-italic.woff
│   │       │       │   │   │   ├── lato-bold-italic.woff2
│   │       │       │   │   │   ├── lato-bold.woff
│   │       │       │   │   │   ├── lato-bold.woff2
│   │       │       │   │   │   ├── lato-normal-italic.woff
│   │       │       │   │   │   ├── lato-normal-italic.woff2
│   │       │       │   │   │   ├── lato-normal.woff
│   │       │       │   │   │   └── lato-normal.woff2
│   │       │       │   │   └── theme.css
│   │       │       │   ├── custom.css
│   │       │       │   ├── doctools.js
│   │       │       │   ├── documentation_options.js
│   │       │       │   ├── file.png
│   │       │       │   ├── jquery-3.5.1.js
│   │       │       │   ├── jquery.js
│   │       │       │   ├── js
│   │       │       │   │   ├── badge_only.js
│   │       │       │   │   ├── html5shiv-printshiv.min.js
│   │       │       │   │   ├── html5shiv.min.js
│   │       │       │   │   └── theme.js
│   │       │       │   ├── language_data.js
│   │       │       │   ├── minus.png
│   │       │       │   ├── plus.png
│   │       │       │   ├── pygments.css
│   │       │       │   ├── searchtools.js
│   │       │       │   ├── underscore-1.12.0.js
│   │       │       │   └── underscore.js
│   │       │       ├── contact.html
│   │       │       ├── genindex.html
│   │       │       ├── help.html
│   │       │       ├── index.html
│   │       │       ├── license.html
│   │       │       ├── log_reg.html
│   │       │       ├── modules.html
│   │       │       ├── objects.inv
│   │       │       ├── search.html
│   │       │       ├── searchindex.js
│   │       │       └── test.html
│   │       ├── conf.py
│   │       ├── contact.rst
│   │       ├── help.rst
│   │       ├── index.rst
│   │       ├── license.rst
│   │       ├── log_reg.rst
│   │       ├── make.bat
│   │       └── modules.rst
│   ├── lg_tools.py
│   ├── log_reg.py
│   └── utils.py
├── test
│   ├── __init__.py
│   ├── test_0.py
│   └── test_cgm.py
└── tools

```
