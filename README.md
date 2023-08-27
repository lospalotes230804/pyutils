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

Inspired in https://github.com/daveoncode/python-utils

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

import pyutils.string as string_utils
email = "example@domain.com"  # Validate if a string is a valid email
if string_utils.is_valid_email(email):
    print(f"{email} es un correo electrónico válido.")
else:
    print(f"{email} no es un correo electrónico válido.")

### String manipulations

### Date validations

import pyutils.date as date_utils
date = "2020-01-01"   # Validate if a string is a valid date
if date_utils.is_valid_date(date):
    print(f"{date} es una fecha válida.")
else:
    print(f"{date} no es una fecha válida.")

### Date Handling

The pyutils.date module offers utilities for date manipulation.

from pyutils import date
formatted_date = date.format_date(date_obj, "yyyy-mm-dd")

### File Operations

The pyutils.file module includes functions for file validation and manipulation based on valid paths.

from pyutils import file
file_size = file.get_file_size("path/to/file.txt")

### Directory Manipulation

The pyutils.dir module provides directory-related functions for validation and manipulation.

from pyutils import dir
dir_contents = dir.list_directory_contents("path/to/directory")

## Contributing

Contributions are welcome! If you have any ideas, bug reports, or feature requests, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contact
For questions or feedback, you can reach us at javalotodo@email.com.
