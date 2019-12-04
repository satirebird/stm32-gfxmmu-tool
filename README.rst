stm32-gfxmmu-tool
=================

Description
-----------

This little tool generates source code for the STM32L4+ GFXMMU peripheral. The GFXMMU
packs the physical memory depending on the shape of the display. For a round display 
the none visible parts are not mapped into memory.


Install
-------

.. code:: bash

    $ git clone https://github.com/satirebird/stm32-gfxmmu-tool.git
    $ cd stm32-gfxmmu-tool
    $ make build

Usage
-----

.. code:: bash

    $ ./venv/bin/stm32-gfxmmu-tool --help
    $ ./venv/bin/stm32-gfxmmu-tool 360 360

Reference
---------

This project based on the template project from Richard Pappalardo.

- `<https://github.com/rpappalax/python-project-template.git>`_
- `<https://www.makotemplates.org/>`_
