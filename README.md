Description:
This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

command interpreter:
 It’s exactly the same as shell but limited to a specific use-case. In our case, we want to be able to manage the objects of our project

 examples:
 Create a new object (ex: a new User or a new Place)
 Retrieve an object from a file, a database etc…
 Do operations on objects (count, compute stats, etc…)
 Update attributes of an object
 Destroy an object
 Cmd.precmd(line)
Hook method executed just before the command line line is interpreted, but after the input prompt is generated and issued. This method is a stub in Cmd; it exists to be overridden by subclasses. The return value is used as the command which will be executed by the onecmd() method; the precmd() implementation may re-write the command or simply return line unchanged.
