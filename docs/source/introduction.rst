.. _introduction:


Installing
==========


.. code:: bash

   pip install sphinx-bulma-theme


Configuring
===========

.. code:: python

   import sphinx_bulma_theme

   html_theme = "bulma"
   html_theme_path = [sphinx_bulma_theme.get_html_theme_path()]

   html_theme_options = {
       'show_topbar': True,
       'topbar_class': 'is-info',
       'topbar_logo_class': 'image is-32x32',
   }


.. seealso:: List with all :ref:`theme options <theme options>`
