########
Activity
########


The `Ballard Locks <https://en.wikipedia.org/wiki/Ballard_Locks>`__ in
Seattle, Washington, are a limited, controlled resource. 

A lock helps vessels to climb and descend hills by creating a pound
with gates at either end. The pound gates are opened to let a vessel enter.
The pound is then flooded (to go up) or drained (to go down). And the vessel 
rises or falls with the water. 

`An explanation of locks <https://en.wikipedia.org/wiki/Lock_(water_navigation)>`_

Note that in the Python code we are using a spelling of Locke to avoid confusion
with a lock!

You have been
hired by the Army Corps of Engineers to help build a software control
system for the locks. There are two locks at the Ballard complex, one
small (30 x 150 feet, 8.5 x 45.7 meter) and one large (80 x 825 feet,
24.4 x 251.5 meter). There are a myriad ways in which different components
of the locks represent limited resources with specialized subsystems,
and a missed or out-of-sequence step could mean disaster. For instance,
there are two sets of doors for each lock, one upstream and one down,
that cannot both be open at the same time; boats need to clear the doors
before they are closed and sealed; pumps need to be shut down before
doors are opened; tourists, who can get very close to observe the
action, need to be safely managed; the locks themselves can only handle
a certain number of boats. At every step of the way there is a limited
resource that must be managed and in lock step with the others, yes, pun
intended. In effect, it involves the coordinated management of resources
all the way down.

For this first task you do not need to model every aspect of the locks,
indeed you only need model its operation overall. Early on you learn
that there will be other software developers interacting with the system
and that not everyone is going to remember all the details of using the
resources of each component. Your task is to model the use of resources,
of system components, as simply as possible. You recognize that with all
the operational and sequencing details to be encapsulated, this is a
good use case for context managers.


Write a context manager class ``Locke`` to simulate the overall
functioning of the system. When the lock is entered it stops the pumps,
opens the doors, closes the doors, and restarts the pumps. Likewise when
the lock is exited it runs through the same steps: it stops the pumps,
opens the doors, closes the doors, and restarts the pumps. Don’t worry
for now that in the real world there are both upstream and downstream
doors, and that they should never be opened at the same time; perhaps
you’ll get to that later. During initialization the context manager class
accepts the lock’s capacity in number of boats. If someone tries to
move too many boats through the lock, anything over its established
capacity, raise a suitable error. Since this is a simulation you need do
nothing more than print what is happening with the doors and pumps, like
this:

::

    "Stopping the pumps."
    "Opening the doors."
    "Closing the doors."
    "Restarting the pumps."


This is how you might interact with your Locke class.

::

    small_locke = Locke(5)
    large_locke = Locke(10)
    boats = 8

    # Too many boats through a small locke will raise an exception
    with small_locke as locke:
        locke.move_boats_through(boats)

    # A lock with sufficient capacity can move boats without incident.
    with large_locke as locke:
        locke.move_boats_through(boats)
