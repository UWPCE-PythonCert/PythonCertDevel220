Office Hours : This weeks' content
==================================
Agenda
------
#. Q+A This week's content
#. Student Demos: This week's content
#. Instructor Demos: This week's content


Lesson 4
========
packaging notes: https://uwpce-pythoncert.github.io/PythonCertDevel/modules/Packaging.html


Lesson 4
========
packaging notes: https://uwpce-pythoncert.github.io/PythonCertDevel/modules/Packaging.html


Missing context for the meta-mailroom exercise.
-----------------------------------------------

Here is some of it.  For starters, I like to use virtualenvs for _everything, always.

```
brew@ontario:~$ which python3
/usr/local/bin/python3
brew@ontario:~$ python3 -V
Python 3.6.5
brew@ontario:~$ mkvirtualenv -p python3 mailroom
Running virtualenv with interpreter /usr/local/bin/python3
Using base prefix '/usr/local/Cellar/python/3.6.5/Frameworks/Python.framework/Versions/3.6'
New python executable in /Users/brew/.virtualenvs/mailroom/bin/python3.6
Also creating executable in /Users/brew/.virtualenvs/mailroom/bin/python
Installing setuptools, pip, wheel...done.
virtualenvwrapper.user_scripts creating /Users/brew/.virtualenvs/mailroom/bin/predeactivate
virtualenvwrapper.user_scripts creating /Users/brew/.virtualenvs/mailroom/bin/postdeactivate
virtualenvwrapper.user_scripts creating /Users/brew/.virtualenvs/mailroom/bin/preactivate
virtualenvwrapper.user_scripts creating /Users/brew/.virtualenvs/mailroom/bin/postactivate
virtualenvwrapper.user_scripts creating /Users/brew/.virtualenvs/mailroom/bin/get_env_details
```
The json_save.zip in the exercise description contains a module. You install it with
```
python setup.py install
```
from within the json_save directory.

```
(mailroom) brew@ontario:/tmp/json_save$ python setup.py install
running install
running bdist_egg
running egg_info
creating json_save.egg-info
writing json_save.egg-info/PKG-INFO
writing dependency_links to json_save.egg-info/dependency_links.txt
writing top-level names to json_save.egg-info/top_level.txt
writing manifest file 'json_save.egg-info/SOURCES.txt'
reading manifest file 'json_save.egg-info/SOURCES.txt'
writing manifest file 'json_save.egg-info/SOURCES.txt'
installing library code to build/bdist.macosx-10.13-x86_64/egg
running install_lib
running build_py
creating build
creating build/lib
creating build/lib/json_save
copying json_save/json_save_meta.py -> build/lib/json_save
copying json_save/saveables.py -> build/lib/json_save
copying json_save/__init__.py -> build/lib/json_save
copying json_save/json_save_dec.py -> build/lib/json_save
creating build/lib/json_save/test
copying json_save/test/__init__.py -> build/lib/json_save/test
copying json_save/test/test_savables.py -> build/lib/json_save/test
copying json_save/test/test_json_save_dec.py -> build/lib/json_save/test
copying json_save/test/test_json_save_meta.py -> build/lib/json_save/test
creating build/bdist.macosx-10.13-x86_64
creating build/bdist.macosx-10.13-x86_64/egg
creating build/bdist.macosx-10.13-x86_64/egg/json_save
copying build/lib/json_save/json_save_meta.py -> build/bdist.macosx-10.13-x86_64/egg/json_save
creating build/bdist.macosx-10.13-x86_64/egg/json_save/test
copying build/lib/json_save/test/__init__.py -> build/bdist.macosx-10.13-x86_64/egg/json_save/test
copying build/lib/json_save/test/test_savables.py -> build/bdist.macosx-10.13-x86_64/egg/json_save/test
copying build/lib/json_save/test/test_json_save_dec.py -> build/bdist.macosx-10.13-x86_64/egg/json_save/test
copying build/lib/json_save/test/test_json_save_meta.py -> build/bdist.macosx-10.13-x86_64/egg/json_save/test
copying build/lib/json_save/saveables.py -> build/bdist.macosx-10.13-x86_64/egg/json_save
copying build/lib/json_save/__init__.py -> build/bdist.macosx-10.13-x86_64/egg/json_save
copying build/lib/json_save/json_save_dec.py -> build/bdist.macosx-10.13-x86_64/egg/json_save
byte-compiling build/bdist.macosx-10.13-x86_64/egg/json_save/json_save_meta.py to json_save_meta.cpython-36.pyc
byte-compiling build/bdist.macosx-10.13-x86_64/egg/json_save/test/__init__.py to __init__.cpython-36.pyc
byte-compiling build/bdist.macosx-10.13-x86_64/egg/json_save/test/test_savables.py to test_savables.cpython-36.pyc
byte-compiling build/bdist.macosx-10.13-x86_64/egg/json_save/test/test_json_save_dec.py to test_json_save_dec.cpython-36.pyc
byte-compiling build/bdist.macosx-10.13-x86_64/egg/json_save/test/test_json_save_meta.py to test_json_save_meta.cpython-36.pyc
byte-compiling build/bdist.macosx-10.13-x86_64/egg/json_save/saveables.py to saveables.cpython-36.pyc
byte-compiling build/bdist.macosx-10.13-x86_64/egg/json_save/__init__.py to __init__.cpython-36.pyc
byte-compiling build/bdist.macosx-10.13-x86_64/egg/json_save/json_save_dec.py to json_save_dec.cpython-36.pyc
creating build/bdist.macosx-10.13-x86_64/egg/EGG-INFO
copying json_save.egg-info/PKG-INFO -> build/bdist.macosx-10.13-x86_64/egg/EGG-INFO
copying json_save.egg-info/SOURCES.txt -> build/bdist.macosx-10.13-x86_64/egg/EGG-INFO
copying json_save.egg-info/dependency_links.txt -> build/bdist.macosx-10.13-x86_64/egg/EGG-INFO
copying json_save.egg-info/top_level.txt -> build/bdist.macosx-10.13-x86_64/egg/EGG-INFO
zip_safe flag not set; analyzing archive contents...
creating dist
creating 'dist/json_save-0.4.0-py3.6.egg' and adding 'build/bdist.macosx-10.13-x86_64/egg' to it
removing 'build/bdist.macosx-10.13-x86_64/egg' (and everything under it)
Processing json_save-0.4.0-py3.6.egg
Copying json_save-0.4.0-py3.6.egg to /Users/brew/.virtualenvs/mailroom/lib/python3.6/site-packages
Adding json-save 0.4.0 to easy-install.pth file

Installed /Users/brew/.virtualenvs/mailroom/lib/python3.6/site-packages/json_save-0.4.0-py3.6.egg
Processing dependencies for json-save==0.4.0
Finished processing dependencies for json-save==0.4.0
```

And now when you check
```
pip list
```

you will see the json_save package.

```
(mailroom) brew@ontario:/tmp/json_save$ pip list
Package          Version
---------------- -------
appnope          0.1.0
backcall         0.1.0
decorator        4.3.0
ipython          6.3.1
ipython-genutils 0.2.0
jedi             0.12.0
json-save        0.4.0  # Here it is!
parso            0.2.0
```
etc....

And now you can use the module to do the exercise.


Question from student:
----------------------
A good question after class on the meta-mailroom exercise.  He was wondering if the json_save package could serialize an object, i.e., an instance of a class he had created in his code.  Short answer, probably not.. at least by my memory of reading through Chris’s code.  The specific case is that the donor db consists of a dictionary where the keys are donor names and the values are objects.  *The json_save module can’t deal directly with the objects in this case… only the native python data types within those objects.*  In other words, the dev would not be able to serialize the whole database dictionary as one json object via the json_save module.  So… the takeaway… it might be easiest to back up in the chronology of mailroom exercises to something before the OO version when you go to work on the meta exercise.

Metaclasses: Definition
=======================
Metaprogramming == writing code in such a way that code is generated (aka "written for you" by the program).

Metaprogramming is popular with code framework developers. This is how you get code generation and smart features in many popular frameworks and libraries (Django, PeeWee, ...).

Metaclass
---------
Metaprogramming in Python uses a special new type of class that is called the metaclass. This type of class, in short, holds the instructions about the behind-the-scenes code generation that you want to take place automatically when another piece of code is being executed.

A metaclass is a class that defines properties of other classes. With a metaclass, we can define properties that should be added to new classes that are defined in our code.

An example:
```
# This metaclass adds a 'hello' method to classes that use the metaclass
# Such classes get a 'hello' method with no extra effort
# The metaclass takes care of that for us

class HelloMeta(type):
    # A hello method
    def hello(cls):
        print("greetings from %s, a HelloMeta type class" % (type(cls())))

    # Call the metaclass
    def __call__(self, *args, **kwargs):
        # create the new class as normal
        cls = type.__call__(self, *args)

        # define a new hello method for each of these classes
        setattr(cls, "hello", self.hello)

        # return the class
        return cls

# Try out the metaclass
class TryHello(object, metaclass=HelloMeta):
    def greet(self):
        self.hello()

# Create an instance of the metaclass. It should automatically have a hello method
# even though one is not defined manually in the class
# in other words, it is added for us by the metaclass
greeter = TryHello()
greeter.greet()
```

The result of running this code is that the new TryHello class is able to printout a greeting that says:

```
greetings from <class '__main__.TryHello'>, a HelloMeta type class
```

The method responsible for this printout is not declared in the declaration of the class. Rather, the metaclass, which is HelloMeta in this case, generates the code at run time that automatically affixes the method to the class.

Rather than get an error for calling a method that does not exist, TryHello gets such a method automatically affixed to it due to using the HelloMeta class as its metaclass.
Metaclasses give us the ability to write code that transforms, not just data, but other code, e.g. transforming a class at the time when it is instantiated. In the example above, our metaclass adds a new method automatically to new classes that we define to use our metaclass as their metaclass.

When Should I Use A Metaclass (Andy's opinion)?
-----------------------------------------------
Never.

Well, perhaps not never. There are problems for which both metaclass and non-metaclass based solutions are available. Usually a non-metaclass solution will be much simpler. But in some cases only metaclass can solve the problem.

99% of the time plain old fashioned inheritance and decorators can get you there just fine with significantly lower complexity.

Metaclasses are very cool but *only use them when you really need them*.

Examples of where only a metaclass will do include creating classes that can only be instantiated once (singletons). Also, creating classes that can’t be subclassed. Some would say they are best used only when creating coding frameworks.


How do metaclasses work?
------------------------
To understand how Python metaclasses work, you need to be very comfortable with the notion of types in Python.
```
>>> name = "andy"
>>> print(type(name))
<class 'str'>
>>> print(type(str))
<class 'type'>
>>> print(type(type))
<class 'type'>
```

metaclass -> instance = class -> instance = object

Remember: every type in Python is defined by a class.

```
>>> class Person:
   pass

>>> andy = Person()
>>> print(type(andy))
<class '__main__.Person'>
```

A class is just another object and can be modified:
```
>>> andy.dob = "2/27/1960"
>>> print(andy.dob)
2/27/1960
```

Hence, Metaclasses modifying classes.

Creating custom Metaclass
-------------------------
In Python you can assign a metaclass to the creation of a new class by passing in the intended masterclass to the new class definition.

The type type, as the default metaclass in Python, defines special methods that new metaclasses can override to implement unique code generation behavior. Here is a brief overview of these "magic" methods that exist on a metaclass:
* ```__new__```: This method is called on the Metaclass before an instance of a class based on the metaclass is created
* ```__init__```: This method is called to set up values after the instance/object is created
* ```__prepare__```: Defines the class namespace in a mapping that stores the attributes
* ```__call__```: This method is called when the constructor of the new class is to be used to create an object

These are the methods to override in your custom metaclass to give your classes behavior different from that of type, which is the default metaclass.

To create our custom metaclass, it must inherit type and will often override:
* ```__new__()```: It’s a method which is called before ```__init__()```. It creates the object and return it. We can override this method to control how the objects are created.
* ```__init__()```: This method initializes the created object passed as parameter


```
# our metaclass
class MultiBases(type):
    # overriding __new__ method
    def __new__(cls, clsname, bases, clsdict):
        # if no of base classes is greator than 1
        # raise error
        if len(bases)>1:
            raise TypeError("Inherited multiple base classes!!!")

        # else execute __new__ method of super class, ie.
        # call __init__ of type class
        return super().__new__(cls, clsname, bases, clsdict)

# metaclass can be specified by 'metaclass' keyword argument
# now MultiBase class is used for creating classes
# this will be propagated to all subclasses of Base
class Base(metaclass=MultiBases):
    pass

# no error is raised
class A(Base):
    pass

# no error is raised
class B(Base):
    pass

# This will raise an error!
class C(A, B):
    pass
```

Note: Decorators can achieve the same code-transformation behavior of metaclasses, but are much simpler.

As quoted by Tim Peters
-----------------------
"Metaclasses are deeper magic that 99% of users should never worry about. If you wonder whether you need them, you don’t (the people who actually need them know with certainty that they need them, and don’t need an explanation about why)."


See https://realpython.com/python-metaclasses/




Missing context for the meta-mailroom exercise.
-----------------------------------------------

Here is some of it.  For starters, I like to use virtualenvs for _everything, always.

```
brew@ontario:~$ which python3
/usr/local/bin/python3
brew@ontario:~$ python3 -V
Python 3.6.5
brew@ontario:~$ mkvirtualenv -p python3 mailroom
Running virtualenv with interpreter /usr/local/bin/python3
Using base prefix '/usr/local/Cellar/python/3.6.5/Frameworks/Python.framework/Versions/3.6'
New python executable in /Users/brew/.virtualenvs/mailroom/bin/python3.6
Also creating executable in /Users/brew/.virtualenvs/mailroom/bin/python
Installing setuptools, pip, wheel...done.
virtualenvwrapper.user_scripts creating /Users/brew/.virtualenvs/mailroom/bin/predeactivate
virtualenvwrapper.user_scripts creating /Users/brew/.virtualenvs/mailroom/bin/postdeactivate
virtualenvwrapper.user_scripts creating /Users/brew/.virtualenvs/mailroom/bin/preactivate
virtualenvwrapper.user_scripts creating /Users/brew/.virtualenvs/mailroom/bin/postactivate
virtualenvwrapper.user_scripts creating /Users/brew/.virtualenvs/mailroom/bin/get_env_details
```
The json_save.zip in the exercise description contains a module. You install it with
```
python setup.py install
```
from within the json_save directory.

```
(mailroom) brew@ontario:/tmp/json_save$ python setup.py install
running install
running bdist_egg
running egg_info
creating json_save.egg-info
writing json_save.egg-info/PKG-INFO
writing dependency_links to json_save.egg-info/dependency_links.txt
writing top-level names to json_save.egg-info/top_level.txt
writing manifest file 'json_save.egg-info/SOURCES.txt'
reading manifest file 'json_save.egg-info/SOURCES.txt'
writing manifest file 'json_save.egg-info/SOURCES.txt'
installing library code to build/bdist.macosx-10.13-x86_64/egg
running install_lib
running build_py
creating build
creating build/lib
creating build/lib/json_save
copying json_save/json_save_meta.py -> build/lib/json_save
copying json_save/saveables.py -> build/lib/json_save
copying json_save/__init__.py -> build/lib/json_save
copying json_save/json_save_dec.py -> build/lib/json_save
creating build/lib/json_save/test
copying json_save/test/__init__.py -> build/lib/json_save/test
copying json_save/test/test_savables.py -> build/lib/json_save/test
copying json_save/test/test_json_save_dec.py -> build/lib/json_save/test
copying json_save/test/test_json_save_meta.py -> build/lib/json_save/test
creating build/bdist.macosx-10.13-x86_64
creating build/bdist.macosx-10.13-x86_64/egg
creating build/bdist.macosx-10.13-x86_64/egg/json_save
copying build/lib/json_save/json_save_meta.py -> build/bdist.macosx-10.13-x86_64/egg/json_save
creating build/bdist.macosx-10.13-x86_64/egg/json_save/test
copying build/lib/json_save/test/__init__.py -> build/bdist.macosx-10.13-x86_64/egg/json_save/test
copying build/lib/json_save/test/test_savables.py -> build/bdist.macosx-10.13-x86_64/egg/json_save/test
copying build/lib/json_save/test/test_json_save_dec.py -> build/bdist.macosx-10.13-x86_64/egg/json_save/test
copying build/lib/json_save/test/test_json_save_meta.py -> build/bdist.macosx-10.13-x86_64/egg/json_save/test
copying build/lib/json_save/saveables.py -> build/bdist.macosx-10.13-x86_64/egg/json_save
copying build/lib/json_save/__init__.py -> build/bdist.macosx-10.13-x86_64/egg/json_save
copying build/lib/json_save/json_save_dec.py -> build/bdist.macosx-10.13-x86_64/egg/json_save
byte-compiling build/bdist.macosx-10.13-x86_64/egg/json_save/json_save_meta.py to json_save_meta.cpython-36.pyc
byte-compiling build/bdist.macosx-10.13-x86_64/egg/json_save/test/__init__.py to __init__.cpython-36.pyc
byte-compiling build/bdist.macosx-10.13-x86_64/egg/json_save/test/test_savables.py to test_savables.cpython-36.pyc
byte-compiling build/bdist.macosx-10.13-x86_64/egg/json_save/test/test_json_save_dec.py to test_json_save_dec.cpython-36.pyc
byte-compiling build/bdist.macosx-10.13-x86_64/egg/json_save/test/test_json_save_meta.py to test_json_save_meta.cpython-36.pyc
byte-compiling build/bdist.macosx-10.13-x86_64/egg/json_save/saveables.py to saveables.cpython-36.pyc
byte-compiling build/bdist.macosx-10.13-x86_64/egg/json_save/__init__.py to __init__.cpython-36.pyc
byte-compiling build/bdist.macosx-10.13-x86_64/egg/json_save/json_save_dec.py to json_save_dec.cpython-36.pyc
creating build/bdist.macosx-10.13-x86_64/egg/EGG-INFO
copying json_save.egg-info/PKG-INFO -> build/bdist.macosx-10.13-x86_64/egg/EGG-INFO
copying json_save.egg-info/SOURCES.txt -> build/bdist.macosx-10.13-x86_64/egg/EGG-INFO
copying json_save.egg-info/dependency_links.txt -> build/bdist.macosx-10.13-x86_64/egg/EGG-INFO
copying json_save.egg-info/top_level.txt -> build/bdist.macosx-10.13-x86_64/egg/EGG-INFO
zip_safe flag not set; analyzing archive contents...
creating dist
creating 'dist/json_save-0.4.0-py3.6.egg' and adding 'build/bdist.macosx-10.13-x86_64/egg' to it
removing 'build/bdist.macosx-10.13-x86_64/egg' (and everything under it)
Processing json_save-0.4.0-py3.6.egg
Copying json_save-0.4.0-py3.6.egg to /Users/brew/.virtualenvs/mailroom/lib/python3.6/site-packages
Adding json-save 0.4.0 to easy-install.pth file

Installed /Users/brew/.virtualenvs/mailroom/lib/python3.6/site-packages/json_save-0.4.0-py3.6.egg
Processing dependencies for json-save==0.4.0
Finished processing dependencies for json-save==0.4.0
```

And now when you check
```
pip list
```

you will see the json_save package.

```
(mailroom) brew@ontario:/tmp/json_save$ pip list
Package          Version
---------------- -------
appnope          0.1.0
backcall         0.1.0
decorator        4.3.0
ipython          6.3.1
ipython-genutils 0.2.0
jedi             0.12.0
json-save        0.4.0  # Here it is!
parso            0.2.0
```
etc....

And now you can use the module to do the exercise.


Question from student:
----------------------
A good question after class on the meta-mailroom exercise.  He was wondering if the json_save package could serialize an object, i.e., an instance of a class he had created in his code.  Short answer, probably not.. at least by my memory of reading through Chris’s code.  The specific case is that the donor db consists of a dictionary where the keys are donor names and the values are objects.  *The json_save module can’t deal directly with the objects in this case… only the native python data types within those objects.*  In other words, the dev would not be able to serialize the whole database dictionary as one json object via the json_save module.  So… the takeaway… it might be easiest to back up in the chronology of mailroom exercises to something before the OO version when you go to work on the meta exercise.

Metaclasses: Definition
=======================
Metaprogramming == writing code in such a way that code is generated (aka "written for you" by the program).

Metaprogramming is popular with code framework developers. This is how you get code generation and smart features in many popular frameworks and libraries (Django, PeeWee, ...).

Metaclass
---------
Metaprogramming in Python uses a special new type of class that is called the metaclass. This type of class, in short, holds the instructions about the behind-the-scenes code generation that you want to take place automatically when another piece of code is being executed.

A metaclass is a class that defines properties of other classes. With a metaclass, we can define properties that should be added to new classes that are defined in our code.

An example:
```
# This metaclass adds a 'hello' method to classes that use the metaclass
# Such classes get a 'hello' method with no extra effort
# The metaclass takes care of that for us

class HelloMeta(type):
    # A hello method
    def hello(cls):
        print("greetings from %s, a HelloMeta type class" % (type(cls())))

    # Call the metaclass
    def __call__(self, *args, **kwargs):
        # create the new class as normal
        cls = type.__call__(self, *args)

        # define a new hello method for each of these classes
        setattr(cls, "hello", self.hello)

        # return the class
        return cls

# Try out the metaclass
class TryHello(object, metaclass=HelloMeta):
    def greet(self):
        self.hello()

# Create an instance of the metaclass. It should automatically have a hello method
# even though one is not defined manually in the class
# in other words, it is added for us by the metaclass
greeter = TryHello()
greeter.greet()
```

The result of running this code is that the new TryHello class is able to printout a greeting that says:

```
greetings from <class '__main__.TryHello'>, a HelloMeta type class
```

The method responsible for this printout is not declared in the declaration of the class. Rather, the metaclass, which is HelloMeta in this case, generates the code at run time that automatically affixes the method to the class.

Rather than get an error for calling a method that does not exist, TryHello gets such a method automatically affixed to it due to using the HelloMeta class as its metaclass.
Metaclasses give us the ability to write code that transforms, not just data, but other code, e.g. transforming a class at the time when it is instantiated. In the example above, our metaclass adds a new method automatically to new classes that we define to use our metaclass as their metaclass.

When Should I Use A Metaclass (Andy's opinion)?
-----------------------------------------------
Never.

Well, perhaps not never. There are problems for which both metaclass and non-metaclass based solutions are available. Usually a non-metaclass solution will be much simpler. But in some cases only metaclass can solve the problem.

99% of the time plain old fashioned inheritance and decorators can get you there just fine with significantly lower complexity.

Metaclasses are very cool but *only use them when you really need them*.

Examples of where only a metaclass will do include creating classes that can only be instantiated once (singletons). Also, creating classes that can’t be subclassed. Some would say they are best used only when creating coding frameworks.


How do metaclasses work?
------------------------
To understand how Python metaclasses work, you need to be very comfortable with the notion of types in Python.
```
>>> name = "andy"
>>> print(type(name))
<class 'str'>
>>> print(type(str))
<class 'type'>
>>> print(type(type))
<class 'type'>
```

metaclass -> instance = class -> instance = object

Remember: every type in Python is defined by a class.

```
>>> class Person:
   pass

>>> andy = Person()
>>> print(type(andy))
<class '__main__.Person'>
```

A class is just another object and can be modified:
```
>>> andy.dob = "2/27/1960"
>>> print(andy.dob)
2/27/1960
```

Hence, Metaclasses modifying classes.

Creating custom Metaclass
-------------------------
In Python you can assign a metaclass to the creation of a new class by passing in the intended masterclass to the new class definition.

The type type, as the default metaclass in Python, defines special methods that new metaclasses can override to implement unique code generation behavior. Here is a brief overview of these "magic" methods that exist on a metaclass:
* ```__new__```: This method is called on the Metaclass before an instance of a class based on the metaclass is created
* ```__init__```: This method is called to set up values after the instance/object is created
* ```__prepare__```: Defines the class namespace in a mapping that stores the attributes
* ```__call__```: This method is called when the constructor of the new class is to be used to create an object

These are the methods to override in your custom metaclass to give your classes behavior different from that of type, which is the default metaclass.

To create our custom metaclass, it must inherit type and will often override:
* ```__new__()```: It’s a method which is called before ```__init__()```. It creates the object and return it. We can override this method to control how the objects are created.
* ```__init__()```: This method initializes the created object passed as parameter


```
# our metaclass
class MultiBases(type):
    # overriding __new__ method
    def __new__(cls, clsname, bases, clsdict):
        # if no of base classes is greator than 1
        # raise error
        if len(bases)>1:
            raise TypeError("Inherited multiple base classes!!!")

        # else execute __new__ method of super class, ie.
        # call __init__ of type class
        return super().__new__(cls, clsname, bases, clsdict)

# metaclass can be specified by 'metaclass' keyword argument
# now MultiBase class is used for creating classes
# this will be propagated to all subclasses of Base
class Base(metaclass=MultiBases):
    pass

# no error is raised
class A(Base):
    pass

# no error is raised
class B(Base):
    pass

# This will raise an error!
class C(A, B):
    pass
```

Note: Decorators can achieve the same code-transformation behavior of metaclasses, but are much simpler.

As quoted by Tim Peters
-----------------------
"Metaclasses are deeper magic that 99% of users should never worry about. If you wonder whether you need them, you don’t (the people who actually need them know with certainty that they need them, and don’t need an explanation about why)."


See https://realpython.com/python-metaclasses/
