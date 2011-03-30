#!/usr/bin/env python

#############################################################################
##
## This file is part of Taurus, a Tango User Interface Library
## 
## http://www.tango-controls.org/static/taurus/latest/doc/html/index.html
##
## Copyright 2011 CELLS / ALBA Synchrotron, Bellaterra, Spain
## 
## Taurus is free software: you can redistribute it and/or modify
## it under the terms of the GNU Lesser General Public License as published by
## the Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.
## 
## Taurus is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU Lesser General Public License for more details.
## 
## You should have received a copy of the GNU Lesser General Public License
## along with Taurus.  If not, see <http://www.gnu.org/licenses/>.
##
#############################################################################

"""
.. currentmodule:: taurus.core.evaluation

Evaluation extension for taurus core model.

The evaluation extension is a special extension that provides evaluation
objects. The official scheme name is 'eval', but 'evaluation' can be used as a synonym.

The main usage for this extension is to provide a way of performing mathematical
evaluations with data from other sources.

The Evaluation Factory (:class:`EvaluationFactory`) uses the following object naming:

    `eval://[evaluator=<evaluatorname>;]<math_expression>[?<symbols>][#<fragment>]`
    
    or:
    
    `eval://evaluator=<evaluatorname>[?<symbols>]`
  
    where:
    
    - The first form of the naming refers to a :class:`EvaluationAttribute` and
      the second form refers a :class:`EvaluationDevice`
  
    - in the first form of the naming, the `evaluator=<evaluatorname>;` is an
      optional segment which defaults to `evaluator=_DefaultEvaluator;` if
      not present.
      
    - `<math_expression>` is a mathematical expression (using python syntax)
      that may have references to other taurus **attributes** by enclosing them
      between `{` and `}`. Expressions will be evaluated by the evaluator device
      to which the attribute is assigned. 
      
    - The evaluator device inherits from :class:`SafeEvaluator` which by default 
      includes a large subset of mathematical functions from the :mod:`numpy`
      module. 
      
    - `<evaluatorname>` is a unique identification name for the evaluator device.
      This allows to use different evaluator objects which may have different
      symbols available for evaluation.
      
    - The optional `?<symbols>` segment is used to provide substitution symbols. 
      `<symbols>` is a semicolon-separated string of `<key>=<value>` strings.
      Before evaluation, the `<math_expression>` string will be searched for
      occurrences of `<key>` which will be replaced by the corresponding
      `<value>` string. If the `?<symbols>` segment is provided in an attribute
      name, the symbols affect only this attribute. If they are defined in a
      device name, they will be available to all attributes of that device. If
      the same `<key>` is defined both in an attribute and its device, the
      `value` defined in the attribute is used.
      
    - The optional `#<fragment>` segment is not (strictly speaking) part of the
      attribute name and is not processed by the Factory. It can be used to
      inform *the client* (e.g. a Taurus widget that uses this attribute as
      its model) that you are interested only in a given fragment (slice) of
      the value of the attribute. Note that if the client does not support this
      convention, this will be silently ignored. The syntax is that of python
      slices (e.g. `[1:-3]`) and will depend on the dimensionality and type of
      the attribute value
      
      

Some examples of valid evaluation models are:

    - An attribute that multiplies a tango attribute by 2:
        
        `eval://2*{tango://a/b/c/d}`
        
    - An attribute that adds two tango attributes together (note we can omit the `tango://` part
      because tango is the default schema in taurus)
      
        `eval://{a/b/c/d}+{f/g/h/i}`
    
    - An attribute that generates an array of random values:
    
        `eval://rand(256)`
        
    - An attribute that adds noise to a tango image attribute:
    
        `eval://{sys/tg_test/1/short_image_ro}+10*rand(*shape({sys/tg_test/1/short_image_ro}))`
        
    - An attribute that uses resources to calculate the voltage from the Intensity and the Resistance:
    
        `eval://{res://I}*{res://R}`
        
    - An evaluator device named `foo`:
    
        `eval://evaluator=foo`
        
    - An evaluator device named `foo` to which 2 custom symbols are assigned 
      (which can be used by any attribute of this device):
    
        `eval://evaluator=foo?bar={tango://a/b/c/d};blah=23`
          
    - An attribute that multiplies `blah` times `bar` (assuming that both `blah`
      and `bar` are known to evaluator `foo`):
        
        `eval://evaluator=foo;blah*bar`
        
    - Same as the previous 2 examples together, but all in one line (the only
      difference is that the symbols defined in this example affect only to this
      attribute, whereas in the example above the symbols were permanently stored
      by the device and thus could be used for other attributes as well):
    
        `eval://evaluator=foo;blah*bar?bar={tango://a/b/c/d};blah=23`

"""
#raise NotImplementedError()
from evalfactory import *