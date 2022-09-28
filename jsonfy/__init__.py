"""
Jsonfy is a python package that takes a data class object and parse it
to a json formated string.
Use the 'packClass' method to get the JSON string of the object\n
Use the 'unpackString' method to get the object from the string\n
\n\n*Notice*\n
The program requiers to take an object which it class is wrapped by the
datacalasses.dataclass function!!
That's because I wanted the let the user know that he cant parse a regular class,'
the methods of the class won't be parsed as well.
If the user won't give an object with the dataclass wrapper, the error:\n
ClassError will be raised.
And the program won't do the crash.
"""
from jsonfy.jsonfy import packObject
from jsonfy.jsonfy import unpackString
from jsonfy.jsonfy import is_dataclass
from jsonfy.jsonfy import dataclass
from jsonfy.jsonfy import ClassError

