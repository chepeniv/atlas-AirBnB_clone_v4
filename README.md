# AirBnB Clone (aka Airbnb, but we’re on a budget)

Welcome to the *"We-Swear-It’s-Not-A-Ripoff"* version of AirBnB. This clone is your gateway to understanding how one of the most famous online rental platforms works—well, sort of. Let’s be honest, we’re not renting out fancy lofts in San Francisco just yet, but stick with us, and you’ll be on your way to mastering some serious Python, object storage, and more... all without ever leaving your couch.

## What is this?
Great question! This project is an attempt at replicating the core functionalities of the beloved AirBnB platform, using Python. Why? Because we like a challenge, and, you know, understanding how things work under the hood is cooler than just booking vacation homes.

Think of this as the scrappy underdog of rental systems. It might not have polished UIs, but we’ve got plenty of Python classes, a command-line interface, and enough object serialization to make even the pickiest database envious.

## How it works (because it actually does)
Here’s how our DIY rental empire is structured:

1. **Models (not the runway type)**: These Python classes handle all the heavy lifting. You’ll find `BaseModel`, `Amenity`, `City`, `Place`, and more. These models know what they are, where they’ve been, and they never forget (thanks to serialization).
   - **BaseModel**: The almighty parent class, because inheritance is cool. Every other class here owes its life to `BaseModel`.
   - **User**: Because someone’s got to book that rental. This is the class for them.
   - **Place**: Where would we be without this? Quite literally nowhere.
   - **City, State**: Geography, but make it code.

2. **File Storage**: Ah yes, our trusty file storage system (`file_storage.py`). It’s the middleman that saves objects to a JSON file (fancy, right?) and reloads them when you least expect it (or ask for it). It’s like the safe in the rental world, except it’s all JSON.

3. **Console**: Step aside, command-line heroes—this is where the magic happens. Through the `console.py`, you can create new users, places, and even cities (if you ever wanted to be mayor). It’s the Pythonic way of Airbnb-ing.

4. **Serialization**: Because Python objects are too cool to exist only in memory. We save them as JSON and pull them back up like a magic trick.

## How to Use It (No Booking Required)
1. **Clone it**: Fork it, clone it, download it—whatever floats your boat. Just get the code on your machine.
   ```bash
   git clone https://github.com/your-github-repo-url.git
   ```

2. **Fire Up the Console**: No, not your game console. Our command interpreter is where the fun begins:

file storage mode:
```bash
./console.py
```

database storage mode:
```bash
sudo sh run_console.sh
```

3. **Create Objects**: Type create followed by the class name and voila! You've just created an instance.

    ```bash
    (hbnb) create User
	```
4. **Show Objects**: Curious about that user you created? Use the show command.

    ```bash
    (hbnb) show User [your-object-id]
	```
5. **All Commands*(*):
* create [class]
* show [class] [id]
* destroy [class] [id] (RIP)
* update [class] [id] [attribute_name] [attribute_value]

## Explanation of How the Console Works:
Here's a breakdown of how the command interpreter (a.k.a. **HBNBCommand**) works, so you can start bossing around your data.

### Imports:
- Import necessary modules and classes, including all model classes you'll be handling.

### Class Definition (HBNBCommand):
- Inherits from `cmd.Cmd`, providing a command-line interface.
- Sets the prompt to `(hbnb)`.
- Defines a dictionary `classes` containing all available model classes.

### Methods:
#### 1. **`do_create(self, arg)`**:
   - **Purpose**: Creates a new instance of a specified class.
   - **Usage**: `create [class]`
   - **Process**:
     - Splits the input arguments.
     - Checks for the class name.
     - Validates if the class exists.
     - Creates a new instance, saves it, and prints the `id`.

#### 2. **`do_show(self, arg)`**:
   - **Purpose**: Shows the string representation of an instance.
   - **Usage**: `show [class] [id]`
   - **Process**:
     - Splits the input arguments.
     - Validates class name and instance ID.
     - Retrieves the object from storage and prints it.

#### 3. **`do_destroy(self, arg)`**:
   - **Purpose**: Deletes an instance based on class name and `id`.
   - **Usage**: `destroy [class] [id]` *(RIP)*
   - **Process**:
     - Validates inputs.
     - Deletes the instance from the storage dictionary and saves changes.

#### 4. **`do_all(self, arg)`**:
   - **Purpose**: Prints all instances of a class, or all instances if no class is specified.
   - **Usage**: `all [class]`
   - **Process**:
     - If a class is specified, validates it and prints instances of that class.
     - If no class is specified, prints all instances.

#### 5. **`do_update(self, arg)`**:
   - **Purpose**: Updates an instance by adding or modifying attributes.
   - **Usage**: `update [class] [id] [attribute_name] [attribute_value]`
   - **Process**:
     - Validates inputs.
     - Sets the new attribute on the instance and saves changes.

#### 6. **`emptyline(self)`**:
   - **Overrides**: Default behavior to do nothing when an empty line is entered.

#### 7. **`do_quit(self, arg)`** and **`do_EOF(self, arg)`**:
   - **Purpose**: Exits the command interpreter.

---

### Error Handling:
- The methods include checks to ensure that the user provides all necessary arguments and that the specified classes and instances exist.
- If an error is detected (e.g., missing class name, invalid class, missing ID), an appropriate error message is printed.

### Storage Interaction:
- The `storage` object is used to interact with the stored data.
- Methods like `storage.new()`, `storage.save()`, and `storage.all()` are used to manage objects.

### Attributes Update:
- In the `do_update` method, `setattr()` is used to dynamically set the attribute on the instance.

### Extensibility:
- The `classes` dictionary can be extended by adding new models.
- Ensure that new model classes are imported at the top and added to the `classes` dictionary.

---

## Example Usage:

    ```bash
    (hbnb) create User
    # Creates a new User instance and prints the id

    (hbnb) show User 1234-1234-1234
    # Prints the string representation of the User instance with id 1234-1234-1234

    (hbnb) destroy User 1234-1234-1234
    # Deletes the User instance with id 1234-1234-1234

    (hbnb) all User
    # Prints all User instances

    (hbnb) update User 1234-1234-1234 email "user@example.com"
    # Updates the email attribute of the User instance with id 1234-1234-1234
	```

And more… just ask the console, it knows things.

## Features (What we aspire to be)
* **CRUD operations**: Create, Read, Update, Delete… the holy grail of data manipulation.
* **Persistence**: Your objects won’t disappear when you quit the console. They’re saved in a JSON file so you can bring them back anytime.
* **Expandability**: You can add cities, places, users, reviews, and even new features. The world is your oyster!

## The Future (Because we’re dreamers)
One day, we dream of having a beautiful front-end, real-time rental bookings, and maybe even a billion-dollar valuation... but until then, you’ve got this neat little console to play around with.

## Contributors (Or... Who to Blame)
* **John Wilson**– Wannabe Python Guru, occasional meme enthusiast.
* **Jose 'Chepe' Olmos** – The one who said “JSON is the way.” i never actually said this
* **AlexAndrea "Ariel" Lopez** -
* **Stephen Newby** – Aspiring High-Level Improviser

    Feel free to fork, contribute, or send us some encouraging words as we slowly inch towards internet stardom. And remember, even if you don't book the place, you can always create it in our console.
