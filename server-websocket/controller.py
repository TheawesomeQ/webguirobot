# In this module, we aim to accomodate the input
#  of any method. This includes inputs
#  from the web gui framework, or any controller
#  that is used with the pygame joystick input.

# To achieve this broad compatibility, we have
#  these requirements:
# - A standard final output for binding our robotics
#   actions to.
# - Data structure for mapping inputs to standard output actions
# - json for configuring mapping


# The AI code solves the input by using an infinite loop
#  and running checks on event type for each event retrieved
#  with the pygame.event.get() method, comparing the attributes
#  of the event (event.type) with constants provided by pygame,
#  such as pygame.JOYAXISMOTION or pygame.JOYBUTTONUP
# We will use the logs from this code to determine the correct inputs from other controllers.

# Our objects:
# - Controller mapper
# - Motor controllers
# - Main program - Load sounds, compute directions from inputs
