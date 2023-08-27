# A Python Utility Library (pyutils)

## Overview

`pyutils` is a Python utility library that provides a collection of helpful functions and modules for common tasks with basic elements, such as:

- String validation & manipulation
- Date validation & manipulation
- File validation & manipulation
- Directory validation & manipulation
- Database validation & manipulation (pending)
- Server validation & manipulation (pending)
- Internet validation & manipulation (pending)

All functions and modules are intended to be SO independent, so they should work on Windows, Linux and Mac OS.

Inspired in https://github.com/daveoncode/python-utils

Please note that
- This is a personal project, so it is not intended to be used in production environments.
- The project is in an early stage of development
- Work is in progress, so code may change without notice
- Testing may not be complete or may not exist at all

Enjoy it and feel free to contribute!

## Requirements

pyutils requires Python 3.6 or higher.

## Installation

You can install pyutils using `pip`:

```bash
pip install pyutils
```

## Use cases

For example, you can use pyutils to validate if a string is a valid email or a valid date.

### String validations

With the validation functions you can validate if a string is a valid email or a valid date.

```python
import pyutils.string.validate as str_val

email = "example@domain.com"  # Validate if a string is a valid email
if str_val.is_email(email):
    print(f"{email} es un correo electrónico válido.")
else:
    print(f"{email} no es un correo electrónico válido.")
```

### String information

With the information functions you can get information about a string, such as the number of words, lines or characters.

```python
import pyutils.string.info as str_info

text = "This is a text"  # Get the number of words in a string
words = str_info.get_words(text)

### String processing

With the processing functions you can process a string, such as, capitalize words, removing accents or escape HTML.

```python
import pyutils.string.process as str_proc

text = "This is a text"  # Capitalize words in a string
capitalized_text = str_proc.capitalize_words(text)
```

### File validations

With the validation functions you can validate if a file is empty, if its writable, if its hidden, if its a JSON file, etc.

```python
import pyutils.file.validate as file_val

file_path = "path/to/file.txt"  # File to validate
if file_val.is_empty(file_path):
    print(f"{file_path} is empty.")
else:
    print(f"{file_path} is not empty.")
```

### File information

With the information functions you can get information about a file, such as the file size, the file extension, the owner, etc.

```python
import pyutils.file.info as file_info

file_path = "path/to/file.txt"  # File to get information
owner = file_info.get_owner(file_path)
```

### File processing

With the processing functions you can process a file, such as, read it, write to it, copy it, duplicate it, archive it with a timestamp, etc.

```python
import pyutils.file.process as file_proc

file_path = "path/to/file.txt"  # File to process
# Duplicate file (adds a sequential number to the file name)
new_path = file_proc.duplicate(file_path) # path/to/file (1).txt
print(f"{file_path} was duplicated to {new_path}.")
# Archive file (adds a timestamp to the file name)
new_path = file_proc.archive(file_path)   # path/to/file_20210321-124351.txt
print(f"{file_path} was archived to {new_path}.")
```

### Directory validations

With the validation functions you can validate if a directory is empty, if its writable, if its hidden, etc.

```python
import pyutils.directory.validate as dir_val

dir_path = "path/to/dir"  # Directory to validate
if dir_val.is_empty(dir_path):
    print(f"{dir_path} is empty.")
else:
    print(f"{dir_path} is not empty.")
```

### Directory information

With the information functions you can get information about a directory, such as the size, its contents, its owner, etc.

```python
import pyutils.directory.info as dir_info

dir_path = "path/to/dir"  # Directory to get information
owner = dir_info.get_owner(dir_path)    # Get the owner of a directory
print(f"{dir_path} is owned by {owner}.")
```

### Directory processing

With the processing functions you can process a directory, such as, create it, delete it, copy it, duplicate it, etc.

```python

## Contributing

Contributions are welcome! If you have any ideas, bug reports, or feature requests, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contact
For questions or feedback, you can reach us at javalotodo@email.com.
