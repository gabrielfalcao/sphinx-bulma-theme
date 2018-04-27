Sphinx Bulma Theme
==================

A Sphinx theme based on the `RTD theme <https://github.com/rtfd/sphinx_rtd_theme>`_, built on top of `bulma.io <https://bulma.io>`_.

`Demo <https://sphinx-bulma-theme.readthedocs.io/>`_

Motivation
----------

Bulma has excellent `content markup <https://bulma.io/documentation/elements/content>`_ and great `message boxes <https://bulma.io/documentation/components/message/#colors>`_ for `admonitions <http://docutils.sourceforge.net/docs/ref/rst/directives.html#admonitions>`_

**WORK IN PROGRESS**



Installing
----------

.. code:: bash

   pip install sphinx-bulma-theme


Configuring
-----------

.. code:: python

   import sphinx_bulma_theme

   html_theme = "bulma"
   html_theme_path = [sphinx_bulma_theme.get_html_theme_path()]


Contributing
------------


.. code:: bash

   pipenv install --dev
   make watch
