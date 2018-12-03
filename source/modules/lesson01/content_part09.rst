##########################
Lesson 01 Advanced Testing
##########################

===========================
Part 9: Integration Testing
===========================

.. toctree::
    :maxdepth: 1

    content_part01
    content_part02
    content_part03
    content_part04
    content_part05
    content_part06
    content_part07
    content_part08
    content_part09
    content_part10
    content_part11

After all this unit testing, it's very tempting to assume that good unit tests
provide everything you need to ensure your code will work properly. That's a
very risky assumption. Even if all the individual elements in your project, there's
always a chance that additional issues will be uncovered when you test the project
as a whole. Let's think a simple example.

How you measure temperature is sometimes a contentious issue. Imagine you have two
developers, working together on a project to read the temperature from a sensor
and use that to control a temperature alarm (a very noisy alarm) that will sound if the
temperature detected is too high. One developer
is American, he works on the code for the thermal sensor class. The other
developer is from England, he is in charge of alarm control class. 

Both developers are very capable and diligent, creating comprehensive unit
tests for their respective classes. In the case of the alarm control class, the
developer used the Mock library to simulate the input coming from the thermal sensor
class. They're both very satisfied that their respective unit tests are passing
and decide to do a live test, that is, with their software connected to both the
thermal sensor and the alarm. The alarm starts sounding right away and the building
has to be evacuated. Oops. What happened?

The American developer coded the sensor class use the Fahrenheit scale, while the
English developer has his alarm control class using Celsius. A typical room 
temperature measurement of 75F would be seen as life-threatening by the alarm
control class, since it thinks the sensor is reporting 75C (167F)

For our integration tests, we want to know if all of our code works
together, as a whole. To accomplish this, we create a calculation
scenario where all of our classes are working together, and confirm that
our calculator produces the correct result.

{{VIDEO HERE}}
