# Jsonfy
## Jsonfy is a python package that takes a data class object and parse it to a json formated string.
You can use it to do the same thing, but in reverse as well.

# The story behind:
I was coding a server and a client, and I needed to transfer a data class called Client from the client to the server.
the data class contained 2 parametrs:
IP:str
MAC:str
(The class was ment to hold the network identify information of a host in a network)
so, I needed some way to transfer the object through the internet.
I knew I could do it using a regular strings, or dicts, but it was a mess and I like to write a clean code.
So, I made a function (on the client side) that takes the object, converting it to a dict and making the dict a json -> called it packObject,
then I coded on the server side a function called unpackString -> takes the string, and reversing the steps of the packObject function.
I decided to share this code with you, and make it a global package so it will be eassier for me to install it on new clients. 

# Notice
## The packObject can only take a dataclassed object as an input
There is no actual reason for this, the program can transfer a regular class parameters but the methods will not be converted.
Therefore to remove any comfusison from your head Im forcing you to use the @dataclass wrapper on the class you want to pack.
A very nice plus is that you keep your code orginaized clean and pro.

The class can convert the following types:<br>
dict ->	object<br>
list, tuple ->	array<br>
str	-> string<br>
int, long, float ->	number<br>
True ->	true<br>
False -> false<br>
None  -> null<br>

# Usage:
A simple packing and unpacking of an object:
```python
import jsonfy

@jsonfy.dataclass # you can use the dataclasses.dataclass as well.
class Dog():
    name:str
    age:int

d = Dog("Rexy", 4)
x = jsonfy.packObject(d) # Converting the object 'd' to a json formatted string.
# x = { "age": 4, "name": "Rexy"}
d_clone = jsonfy.unpackString(x) # Converting the string 'x' to a dog object
print(d.name)
print(d.age)
```
output:
```bash
Rexy
4
```

# _Hope yall having a good day!_"