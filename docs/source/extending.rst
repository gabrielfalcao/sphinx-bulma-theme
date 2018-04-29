.. _extending:


Extending the Theme
===================

This theme makes efforts to be as extensible as possible.

In this guide we will learn how to modify docutils nodes before
rendering, tweak CSS and apply javascript hacks.


Install Dependencies
--------------------

**We will need:**

- nodejs v9.11.1 or superior
- npm 5.8.0 or superior

.. code:: bash

   # clone the repo
   git clone https://github.com/gabrielfalcao/sphinx-bulma-theme.git

   cd sphinx-bulma-theme
   npm install --dev



Customizing CSS and JS
----------------------

Sphinx has its own opinion of what CSS classes should be in what elements.
The theme attempts to inject the appropriate classes in certain nodes through :py:func:`sphinx_bulma_theme.bulmanize_documentation`.

But that's not enough.

To bridge the gap between bulma styles and Sphinx's optionated CSS classes this theme uses special CSS and Javascript.

Don't worry it's not as bad as it sounds.

Looking at the source tree we can spot 2 files:

- ``sphinx_bulma_theme/sphinx-bulma.src.sass``
- ``sphinx_bulma_theme/sphinx-bulma.src.js``


sphinx-bulma.src.sass
~~~~~~~~~~~~~~~~~~~~~

The good news: Bulma is build on `sass
<https://github.com/jgthms/bulma/blob/master/bulma.sass>`_ so this
theme makes little effort in extending it.

To build the CSS file run:

.. code:: bash

   make sass

Under the hood it will run:

.. code:: bash

   node-sass --include-path scss sphinx_bulma_theme/sphinx-bulma.src.sass sphinx_bulma_theme/static/css/theme.css


sphinx-bulma.src.js
~~~~~~~~~~~~~~~~~~~

The good news: ES6 support :)

To build the JS file run:

.. code:: bash

   make webpack

Under the hood it will run:

.. code:: bash

   export NODE_ENV=production
   export NODE_PATH=.:./node_modules:./sphinx_bulma_theme:$NODE_PATH
   webpack -p


Customizing Python Transformations
----------------------------------


We will modify the file ``sphinx_bulma_theme/__init__.py``.

The execution entrypoint we will look for is :py:func:`~sphinx_bulma_theme.bulmanize_documentation`

.. seealso:: :py:func:`sphinx_bulma_theme.add_classes_to_node` and :py:func:`~sphinx_bulma_theme.process_admonition_node`
