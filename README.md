# Website Generator
A Python script that generates HTML code for my personal website by using data from a JSON file, and replacing placeholders in an HTML template.


## How to use

</br>

- Editing the JSON file:
    - Make any desired changes under the relevant key in the `webcontent.json` file.
    - Execute the `main.py` script.
    - `index.html` file should generate in the script directory.

</br>

- Without editing the JSON file:
    - Make any desired changes under the relevant key in the `to_json()` function in the `main.py` file.
    - At the very bottom of the `main.py` file, in the `if __name__ == "__main__"` statement, remove the comment from the `to_json` function call.
    - Execute the `main.py` script.

</br>

- **Note**: The generated JSON and HTML files will work right after they are generated, but are not formatted properly. You can easily format them in a readable format using VS Code by pressing `Shift + Alt + F` (default Windows shortcuts).

</br>

I am leaving my personal details in the script and JSON files as an example of the required format. For the assets, scripts and styles files, please visit my personal [website repo](https://github.com/AntonisTorb/AntonisTorb.github.io). Thank you!