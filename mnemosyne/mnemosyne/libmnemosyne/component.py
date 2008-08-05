##############################################################################
#
# component.py <Peter.Bienstman@UGent.be>
#
##############################################################################



##############################################################################
#
# Component
#
#   The base class of everything that can be plugged together and swapped
#   out to realise the core functionality of Mnemosyne.
#
#
##############################################################################

class Component(object):

    ##########################################################################
    #
    # __init__
    #
    ##########################################################################

    def __init__(self, name="", description=""):
        
        self.name        = name
        self.description = description