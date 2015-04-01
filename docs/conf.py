# -*- coding: utf-8 -*-
#
# scikit-neuralnetwork documentation build configuration file, created by
# sphinx-quickstart on Tue Mar 31 20:28:10 2015.

import sys
import os

project = u'scikit-neuralnetwork'
copyright = u'2015, scikit-neuralnetwork developers (BSD License)' 


# -- Overrides for modules ----------------------------------------------------

from mock import Mock as MagicMock

class Mock(MagicMock):
    @classmethod
    def __getattr__(cls, name):
        return Mock()

MOCK_MODULES = ['numpy', 'theano', 'sklearn', 'pylearn2']
sys.modules.update((mod_name, Mock()) for mod_name in MOCK_MODULES)


# -- Configuration of documentation -------------------------------------------

sys.path.append(os.path.dirname(os.path.dirname(__file__)).encode('utf-8'))

import sknn
version = sknn.__version__
release = sknn.__version__

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.coverage', 'numpydoc']
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
exclude_patterns = ['_build']

pygments_style = 'sphinx'
todo_include_todos = False


# -- Options for HTML output --------------------------------------------------

html_title = 'scikit-neuralnetwork documentation'
# html_logo = 'img/logo.png'
# html_favicon = 'img/favicon.ico'

html_static_path = ['_static']
htmlhelp_basename = 'sknndoc'
