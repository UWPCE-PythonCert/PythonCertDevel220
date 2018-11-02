=======================
Python 220 Week 10 Quiz
=======================


#. Which of these types are not "regular objects" in Python?
Integers
Strings
Functions created with "def"
Class Instances
Classes created with "class"

All of them! Everything in Python is an object -- they can be assigned names, passed to functions, introspected, etc.

#. setattr(object, att_name, att_value) Is exactly the same as
object.att_name = att_value

True
False

Not quite!
setattr(object, att_name, _att_value) lets you use ANY string as an
att_name -- even ones that aren't legal python names. Try:&lt;/p&gt;
&lt;pre class="p1"&gt;&lt;span class="s1"&gt;setattr&lt;/span&gt;&lt;span class="s2"&gt;(c, &lt;/span&gt;&lt;span class="s3"&gt;"3-4"&lt;/span&gt;&lt;span class="s2"&gt;, &lt;/span&gt;&lt;span class="s3"&gt;"fred"&lt;/span&gt;&lt;span class="s2"&gt;)&lt;/span&gt;&lt;/pre&gt;
&lt;p class="p1"&gt;&lt;span class="s2"&gt;it'll work! But you'll need to use:&lt;/span&gt;&lt;/p&gt;
&lt;pre class="p1"&gt;&lt;span class="s1"&gt;getattr&lt;/span&gt;&lt;span class="s2"&gt;(c, &lt;/span&gt;&lt;span class="s3"&gt;'3-4'&lt;/span&gt;&lt;span class="s2"&gt;)&lt;/span&gt;&lt;/pre&gt;
&lt;p class="p1"&gt;&lt;span class="s2"&gt;to access it.&lt;/span&gt;&lt;/p&gt;
&lt;p&gt; &lt;/p&gt;

#. An object's: __dict__ Is always an actual dictionary
True
False

Sort of:&lt;/p&gt;
&lt;p&gt;sometimes &lt;/p&gt;
&lt;pre&gt;__dict__&lt;/pre&gt;
&lt;p&gt;returns a "Mapping Proxy" -- which is essentially a read-only dict.&lt;/p&gt;
&lt;p&gt;So you can always treat __dict__ as a dict for reading, but you may not be able to write to it.&lt;/p&gt;
&lt;p&gt;use setattr() to set an attribute, rather than trying to write to its __dict__. &lt;/p&gt;

#. What is the class of a class object (created with the class keyword)?&lt;/div&gt;
type: class
type: object
type: metaclass
type: type
The type of a class object is "type" -- "class" and "type" mean the same thing in Python.

#. Which of these special methods is run first when you create a new class object with a metaclass?&lt;/p&gt;
&lt;p&gt; &lt;/p&gt;
&lt;/div&gt;
__new__
__init__

#. Using metaclasses or class decorators can impact performance, as there is extra code being run every time you make a new instance of a  class.&lt;/div&gt;
True
False
metaclasses and class decorators are both applied at module import time: when the class object is created. So there is no real overhead at runtime, when new instances are created -- or when instances are used.
