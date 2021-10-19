Foremast - foremast-templates Example
=====================================

This is a repository that is used for providing example Foremast templates.

By default, Foremast comes bundled with default templates but they can all be overridden with external templates! This is great for individual companies to extend foremast functionality and also override the defaults to company specific values/naming conventions. This repository acts as examples for how the external templates can be structured.

Getting Started
---------------

Take a look at `quick start guide`_ for a quick introduction on how to use
Foremast.

We also have a blog post to help you get started: `Automate Spinnaker Pipeline Creation`_

Documentation
~~~~~~~~~~~~~

All the documentation can be viewed on `Read the Docs`_. You can find all
configuration options, code information, and better examples there.

Development
~~~~~~~~~~~

See the `contribution guide`_ for information on code style, contributing, and
testing.

Getting Help
~~~~~~~~~~~~~

For questions, support, or friendly conversation you can find us on `Gitter`_.

External Foremast Templates
~~~~~~~~~~~~~~~~~~~~~~~~~~~

In the foremast configuration file (`config.py`), add a `templates_path` key. You can see an example of this in the example [config.py](configs/config.py) This can be an absolute value or a path relative to where you are running Foremast. The value of this config key should be the path to the directory which holds the external Foremast templates.

The structure of your templates directory should match the defaults provided with Foremast. The names of the files also need to be the same with the exception of pipeline stages.

.. _`quick start guide`: http://foremast.readthedocs.io/en/latest/getting_started.html#quick-start-guide
.. _`automate spinnaker pipeline creation`: https://tech.gogoair.com/foremast-automate-spinnaker-pipeline-creation-2b2aa7b2c5e4#.qplfw19cg
.. _`Read the Docs`: http://foremast.readthedocs.io/en/latest/
.. _`contribution guide`: http://foremast.readthedocs.io/en/latest/CONTRIBUTING.html
.. _`Gitter`: https://gitter.im/foremast/foremast