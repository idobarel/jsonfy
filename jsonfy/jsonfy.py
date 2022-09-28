import json
from dataclasses import dataclass, is_dataclass

class ClassError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

def packObject(o:object)->str:
    """
    Pack the object 'o' into a json formated string.
    """
    if not is_dataclass(o):
        raise ClassError("The speciffied class must be of type dataclass.")
    d = o.__dict__
    return json.dumps(d, sort_keys=True, indent=4)

def unpackString(s:str)->object:
    """
    Unpack the json string 's' into an object
    """
    d = json.loads(s)
    @dataclass
    class JSONFYOutput():
        def __init__(self) -> None:
            self.__dict__.update(d)
    obj = JSONFYOutput()
    return obj
