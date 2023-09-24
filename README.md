# GPyLang - ChatGPT Powered Script Language

### <center>[中CN](README_CN.md)/[EN](README.md)</center>

GPyLang is a programming language powered by ChatGPT, designed to have a Python-like syntax with some unique features. As a compiler for GPyLang, it follows specific rules and conventions to translate GPyLang code into standard Python code.

## Syntax and Keywords

GPyLang closely resembles Python but introduces new keywords to extend its functionality:

- `use`: Use to ask compiler implement a function you described. For example: `use deleteFile\ndeleteFile("test.txt")`.

- `gen:[type]`: This keyword quickly builds variables. For instance:
  - `files = gen:[list(str)]("all files in this directory")`.
  - `nums = gen:[list(int)]("all perfect square numbers under 100")`.

- `chat`: This keyword retrieves responses from ChatGPT and replaces the return value with the answer in the code. For example:
  ```python
  print(chat("who are u")) #result is GPYLang Compiler
  ```

## Example Usage

Here's an example of how the GPyLang compiler should behave:
```
User Input:
print(chat:[bool]("Is China a country of Asia?"))
print(gen:[list(int)]("Numbers within 100 that are divisible by 2"))

Compiler Output:
{
    "status": 0,
    "message": "success!",
    "code": "print(True)\nprint([x for i in range(100) if x % 2 == 0])"
}
```

In this example, the user input contains GPyLang code, and the compiler provides a JSON response with the translated Python code and a success message.

## Installation

To install GPyLang, run the following command(not implemented):

```
pip install gpylang
```

## Generating and Running Your Script

Please note that the following functionality is not yet implemented.

In the future, to generate and run your GPyLang script, you can use the following command:

```
gpy filename.gpy -o output.py
```

## Contribution

As a current student, my available time for development is limited. If you wish to contribute to this project, please consider submitting a Pull Request (PR) or creating an issue.

Thank you for expressing your interest in GPyLang, and please stay updated for future announcements!

## Donations

We are not currently accepting donations for this project.