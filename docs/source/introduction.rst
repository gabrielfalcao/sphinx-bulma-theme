.. _introduction:


Install
=======


.. code:: bash

   pip install sphinx-bulma-theme


.. seealso:: Various message colors available
.. warning:: Too much fun ahead
.. tip:: write docs
.. note:: attention to detail


Configure Theme
===============

.. code:: python

   import sphinx_bulma_theme

   html_theme = "bulma"
   html_theme_path = [sphinx_bulma_theme.get_html_theme_path()]



Configure Extension
===================

.. code:: python

   extensions = [
       'sphinx.ext.autodoc',
       'sphinx.ext.doctest',
       'sphinx.ext.intersphinx',
       'sphinx.ext.viewcode',
       'sphinx.ext.githubpages',
       # ...
       'sphinx.ext.bulma',
   ]
