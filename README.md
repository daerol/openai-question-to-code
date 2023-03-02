# OpenAI Question to Code

I've created a tool that can generate code solutions for educational purposes. It's powered by OpenAI's text-davinci-002 model, which means you can input a coding challenge and the tool will generate a code solution for you. Please keep in mind that the generated code solutions are meant to serve as a reference only, and may not be 100% accurate. Use the tool with caution and at your own risk.


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements file.

```bash
pip install -r requirements.txt
```

## Environment file

```python
DIRECTORY=
PATH_TO_TESSERACT=/usr/local/bin/tesseract
OPENAI_APIKEY=
DEFAULT_LANGUAGE=
DEFAULT_ENGINE=
DEFAULT_MESSAGE_PROMPT=
TESSERACT_CONFIG=-c preserve_interword_spaces=1 --psm 1 --oem 1
```


## How it works
Here's how the tool works:

1. First, you'll need to take a screenshot of the coding challenge you want to solve and save it in the image folder. Then, the tool will read your input and generate code output based on the language you select in the environment file.

1. First, it checks if the images folder exists. If it does, the tool will loop through all the images from 0.png to the last numbered image. Each time the loop runs, it reads the image and converts it to text using Tesseract OCR. The resulting text is then appended in numerical order to a text file named "problem.txt".

2. Next, the tool concatenates the default prompt message with the contents of problem.txt. The default prompt message is then fed into OpenAI, along with the language specified in the environment file. OpenAI will then generate a function based on the input and the selected language.

3. Once OpenAI returns the generated code solution, it will be written to a file named "solution". The file type will be determined by the DEFAULT_LANGUAGE setting.

## How to run

To use this tool, there are a few steps you need to follow:

1. First, you'll need to install the required dependencies. You can do this by running "pip install -r requirements.txt" in your terminal.

2. Make sure you have image files in the images folder. Remember that the first image file should be named "0.png", and subsequent images should be numbered incrementally (e.g. "1.png", "2.png", etc.).

3. Create a .env file and include the necessary flags. This file should be placed in the same directory as the main.py file. Make sure to include the language flag and the file extension for the output file.

4. Finally, you can run the tool by executing "python main.py" in your terminal.

## Things to note
The tool uses a loop that starts from 0, which means that the first image file it looks for is 0.png. If your image files are not numbered starting from 0, the tool won't be able to find them and generate code solutions.

For example, if you have an image file named "screenshot_1502121.png", you'll need to rename it to "0.png" before using the tool. Then, for each additional image file, you'll need to increment the number by 1 (e.g. "1.png", "2.png", and so on).

