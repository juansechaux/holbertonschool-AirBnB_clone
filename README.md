# AIRBNB CONSOLE
---
<img src="/pictures/console.png" border="0">

# Welcome to AIRBNB Clone project 

> This is the first step to build a web application AIRBNB clone.

> We will start with the construction of a console or command interpreter, with the base model as an entry point and other classes, we will be able to use the console to create the data model that will allow to create, update, destroy, display, store and persist objects to a file.JSON file. 

## Table of Contents
---
- Objetives
- Requeriments
- Installation and execution
- Console commands
- Tests
- Authors

## Objectives
---
* How to create a Python package
* How to create a command interpreter in Python using the cmd module
* What is Unit testing and how to implement it in a large project
* How to serialize and deserialize a Class
* How to write and read a JSON file
* How to manage datetime
* What is an UUID
* What is *args and how to use it
* What is **kwargs and how to use it
* How to handle named arguments in a function

## Requeriments
> All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)

## Usage
### Installation and execution

- Clone the repository
> $ git clone git@github.com:ricardovaldesv/holbertonschool-AirBnB_clone.git
* Execute the console file
> /holbertonschool-AirBnB_clone# ./console.py 


### Console commands
---
The commands available for this command interpreter are:

| Name       | Description   |
| ---------- | ------------- |
|**create*| Creates a new instance of the class passed by argument.|
|*show*| Prints the string representation of an instance.                                        |
|**destroy*| Deletes an instance that was already created.                                           |
|*all*| Prints string representation of all instances or of all instances of a specified class. |
|**update*| Updates an instance attribute if exists otherwise create it.                            |
|*help*| Show all commands or display information about a specific command.|
|*quit*| Exit the console.|
|*EOF*| Exit the console.|

**create, destroy and update commands save changes into a JSON file.*

### Commands usage: 


| *Command*  | *Usage* |
| -------- | -------- |
|*create*  | ***create*** <class_name>|
|*show*    | ***show*** <class_name> <object_id> **|
|*destroy* | ***destroy*** <class_name> <object_id **|
| *all*    | **all** <class_name> **|
| *update* | ***update*** <class_name> <object_id> <attribute name> "<attribute value>" **|
| *help*   | ***help*** **;** ***help*** <command_name>|
| *quit*   | ***quit*** |
| *EOF*    | ***EOF*** **;** (ctrl + d)|

## Tests ⚙️
---

### Interactive Mode ⌨️

#### Example 1: Using create and all commands
```
root@e4aa8294c3aa:~/holberton/holbertonschool-AirBnB_clone# ./console.py 
(hbnb) all
[]
(hbnb) create User
e124e440-7850-4663-a227-92df2e743b5c
(hbnb) create BaseModel
e87335bb-ec4d-41d1-8498-60e2eb9ff8dc
(hbnb) all
["[User] (e124e440-7850-4663-a227-92df2e743b5c) {'id': 'e124e440-7850-4663-a227-92df2e743b5c', 'created_at': datetime.datetime(2023, 11, 6, 18, 0, 0, 651068), 'updated_at': datetime.datetime(2023, 11, 6, 18, 0, 0, 651068)}", "[BaseModel] (e87335bb-ec4d-41d1-8498-60e2eb9ff8dc) {'id': 'e87335bb-ec4d-41d1-8498-60e2eb9ff8dc', 'created_at': datetime.datetime(2023, 11, 6, 18, 0, 21, 347088), 'updated_at': datetime.datetime(2023, 11, 6, 18, 0, 21, 347088)}"]
(hbnb) 
```

#### Example 2: Using basic update with an Id and show command

```
(hbnb) update BaseModel e87335bb-ec4d-41d1-8498-60e2eb9ff8dc first_name "Ricardo"
Ricardo
<class 'str'>
(hbnb) show BaseModel e87335bb-ec4d-41d1-8498-60e2eb9ff8dc
[BaseModel] (e87335bb-ec4d-41d1-8498-60e2eb9ff8dc) {'id': 'e87335bb-ec4d-41d1-8498-60e2eb9ff8dc', 'created_at': datetime.datetime(2023, 11, 6, 18, 0, 21, 347088), 'updated_at': datetime.datetime(2023, 11, 6, 18, 2, 12, 656122), 'first_name': 'Ricardo'}
(hbnb)
```

#### Example 3: Using destroy and count command
```
(hbnb) destroy BaseModel e87335bb-ec4d-41d1-8498-60e2eb9ff8dc
(hbnb) all
["[User] (e124e440-7850-4663-a227-92df2e743b5c) {'id': 'e124e440-7850-4663-a227-92df2e743b5c', 'created_at': datetime.datetime(2023, 11, 6, 18, 0, 0, 651068), 'updated_at': datetime.datetime(2023, 11, 6, 18, 0, 0, 651068)}"]
(hbnb) 
```

## AUTHORS
- [Juan Sebastian Varcarcel Chaux](https://github.com/juansechaux)
- [Ricardo Valdes Vidal](https://github.com/ricardovaldesv)