HED Test Suite
==============

.. sidebar:: Quick links
   
   * `HED homepage <https://www.hedtags.org/>`_ 

   * `HED specification <https://www.hedtags.org/hed-specification>`_ 

   * `Python validator <https://github.com/hed-standard/hed-python>`_

   * `JavaScript validator <https://github.com/hed-standard/hed-javascript>`_

   * `HED schemas <https://github.com/hed-standard/hed-schemas>`_

   * `HED organization <https://github.com/hed-standard/>`_  

Welcome to the HED Test Suite documentation! This repository provides the **official JSON test cases**
for validating HED (Hierarchical Event Descriptors) validator implementations across all platforms.
These version-controlled tests ensure consistent validation behavior across all HED validator
implementations. he tests are designed to:

* **Validate validators**: Ensure Python, JavaScript, and future implementations produce consistent results
* **Specify behavior**: Provide machine-readable examples of HED validation rules  
* **Enable AI training**: Include structured explanations and correction examples for AI systems
* **Prevent regressions**: Catch validation changes across versions

Key Features
------------

* **Comprehensive coverage**: 136 test cases covering 33 error codes
* **Multiple test types**: String, sidecar, event, and combo tests
* **AI-friendly**: The tests include explanations and correction strategies
* **Cross-platform**: Single source of truth for all validator implementations
* **Automated validation**: JSON schema validation ensures test quality


.. toctree::
   :maxdepth: 2

   User guide <user_guide>

Test suite reports
-------------------------

.. toctree::
   :maxdepth: 2

   Test coverage report <test_coverage>
   Test index <test_index>


* :ref:`genindex`
