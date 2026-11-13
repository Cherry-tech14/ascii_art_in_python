# ASCII Art Generator (Python)

A command-line program written in Python that takes a text string as an argument and outputs a graphical representation of the string using ASCII characters.

## 🚀 Features

- **Multiple Font Styles:** Supports three distinct banner templates (`standard`, `shadow`, and `thinkertoy`).
- **Newline Handling:** Fully supports explicit newlines (`\n`, `\n\n`) to generate multi-line art.
- **Special Characters & Numbers:** Handles uppercase, lowercase, digits, spaces, and punctuation correctly.
- **Modular Architecture:** Clean separation of concerns across different Python modules for maintainability and readability.


## 📂 Project Structure

### text
ascii-art/
│
├── main.py          # Entry point handling command-line arguments and execution
├── render.py        # Core logic for slicing, mapping, and stitching ASCII rows
├── banner.py        # File reader and parser for banner files
├── standard.txt     # Standard font banner file
├── shadow.txt       # Shadow font banner file
├── thinkertoy.txt   # Thinkertoy font banner file
└── README.md        # Project documentation

## Installation & Setup

* Clone or Download this repository into your local machine.

* you have Python 3 installed.

* Make sure all three Python scripts (main.py, render.py, banner.py) and your banner text files (standard.txt, shadow.txt, thinkertoy.txt) are in the same project directory.


## Usage

* Run the program from your terminal by passing a string and an optional banner style:
Bash

* python3 main.py "<your-string>" [banner-style]

## Examples:

* Using the default standard banner:
    Bash

* python3 main.py "Hello"

* Using the shadow banner:
    Bash

* python3 main.py "Hello There" shadow

* Using the thinkertoy banner:
    Bash

* python3 main.py "123" thinkertoy

*Handling newlines (\n):
    Bash

* python3 main.py "Hello\nWorld"

* Testing with cat -e (to check trailing spaces/newlines):
    Bash

* python3 main.py "Hello" | cat -e

## How It Works

* banner.py: Opens the requested .txt banner file, reads its lines, and slices out the exact 8-line graphic blocks for printable ASCII characters (from ASCII 32 to 126).

* render.py: Splits input text by user-defined newlines, loops through each of the 8 character rows horizontally, and stitches the characters side-by-side.

* main.py: Interacts with the user via command-line arguments (sys.argv), invokes the rendering engine, and prints the final output to the console.