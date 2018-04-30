.. _mermaid:

sphinxcontrib-mermaid
=====================

`extension docs <https://sphinxcontrib-mermaid-demo.readthedocs.io/en/latest/>`_

.. mermaid::

   sequenceDiagram
      participant Alice
      participant Bob
      Alice->John: Hello John, how are you?
      loop Healthcheck
          John->John: Fight against hypochondria
      end
      Note right of John: Rational thoughts <br/>prevail...
      John-->Alice: Great!
      John->Bob: How about you?
      Bob-->John: Jolly good!
