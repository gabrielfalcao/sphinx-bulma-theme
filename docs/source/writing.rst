.. _writing:


Writing Python Documentation
============================

The very idea of writing documentation sounds tedious to some, this
guide aims to remove mental blocks by synthesizing some of the most
common tasks for writing documentation.

By the end of the guide you will know:

- Boostrap Sphinx documentation
- Configure a theme
- Document python modules internally with docstrings
- Reference documented parts of the code: *(modules, classes, methods, etc)*
- Make the reverse-reference: your code linking to the documentation
- Auto-generate API-reference page for python modules
- Use :py:mod:`sphinx.ext.intersphinx` to reference external modules documented with Sphinx (e.g.: *Flask, requests, boto3*)


Annotating Code
---------------



Sphinx ships with the :py:mod:`sphinx.ext.autodoc` which generates the classic API Reference section of many known open source libraries such as `Flask <http://flask.pocoo.org/docs/latest/api/>`_, `requests <http://docs.python-requests.org/en/master/api/>`_ and `boto3 <https://boto3.readthedocs.io/en/latest/reference/core/boto3.html>`_.


Functions
~~~~~~~~~


**Example Code**

.. code:: python


   def make_user(email, password, admin=False, **kwargs):
       """creates structured user data for storage

       :param email: string
       :param password: in plain-text
       :param admin: bool - indicates user has all priviledges
       :param kwargs: extra data

       :returns: a :py:class:`dict` with user data
       """
       data = locals()
       data.update(data.pop('kwargs'))
       return data



**Reference function in a rst document**


.. code:: rst

   .. autofunction:: sphinx_bulma_theme.example.make_user


**Rendered HTML:**



.. autofunction:: sphinx_bulma_theme.example.make_user
