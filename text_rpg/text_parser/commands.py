"""Serves as the base command class for all command types.

Commands are the actions available to the player. Used to get information
about commands and to evaluate them for the parser. 
"""

#from events.system_events import ErrorEvent

# TODO: This or generate from docs? (To gen from docs use func.__help__ for doc string text, func.__name__ - Command for func name, func.__annotations__ for types,  
class Parameter:
    value: any = None
    type: type = None # TODO: How do I handle this?
    description: str = "No description has been provided for this parameter."


class BaseCommand:
    """Base command class that all other commands should inherit.

    Attributes:
        description_text: Instructions on how to use the command.
    """
    # TODO: Include private attributes above?
    # TODO: I'm following this convention right?
    _help_text = "No help text has been given to this command."
    _params: list[Parameter] # Each param needs name, type, ordering?, description, auto generate from docs + function declaration?

    def evaluate(self, args: list[str]): #-> ErrorEvent:
        """Evaluates meaning of command."""
        #return ErrorEvent("Using base command evaluation which should not be used.")

    @classmethod
    def get_help_text(cls) -> str:
        """Returns formatted help text for this command."""
        # TODO: Should this be static? shoudl you need to instance this?
        # TODO: YES MOVE INTO FUNCTION THAT USES DATA IN THE CLASS AND THEN IS CALLED ON IT (EX: GET_HELP_TEXT(COMMAND))
        usage_text: str = 
        print(usage_text)
        return ("FORMAT USAGE TEXT WITH PARAMS AND DESCRIPTION OF ARGS BELOW, DESCRIPTION OF COMMAND BELOW THAT"
            # TODO: How to print multiline like this and how am i going to get parameters?
        ) 
    
    BaseCommand.evaluate

class HelpCommand:
    """Command that displays some useful actions to the user.
    
    Attributes:
        help_text: Instructions on how to use the help command.
    """
    # TODO: Format help text to match terminal syntax
    help_text = "usage: help" # This should be generated from docs

class ClearCommand:
    """Command that clears the main output window.
    
    Attributes:
        help_text: Instructions on how to use the clear command.
    """
    help_text = "usage: clear"
    # TODO: Have autoformatter for help text that is in base, formats arguments, for usage example and formats insctructions, etc

class QuitCommand:
    """"""