'''
This is created for pure educational purposes, the script uses openAI's code-davinci-002 model generate code from a prompt. You can use text-davinci-002 to generate code too, but the code generated is not as good as code-davinci-002.

You are required to have an openAI account and API key to run this script.
And .env file with the following variables:
- OPENAI_APIKEY (required)
- DIRECTORY (optional)
- PATH_TO_TESSERACT (optional)
- DEFAULT_MESSAGE_PROMPT (optional)
- DEFAULT_ENGINE (optional) 
- DEFAULT_LANGUAGE (optional)

The script will iterate through all image in the directory given and concatenating all the image text to generate code.
'''


# OpenAI is to load the codex model and call the API to summarise the text. The code is as follows:
import openai
# PIL is to open the image and pytesseract is to extract the text from the image
import pytesseract
import PIL.Image
# os is to retrieve env variables and glob is to iterate through all files in a directory
import os
from pathlib import Path
# dot env
from dotenv import load_dotenv

load_dotenv()

# os. config
DIRECTORY = os.getenv("DIRECTORY") or str(Path.cwd())
PATH_TO_TESSERACT = os.getenv("TESSERACT_PATH")
OPENAI_APIKEY = os.getenv("OPENAI_APIKEY")
DEFAULT_LANGUAGE = os.getenv("DEFAULT_LANGUAGE") or "python"
DEFAULT_ENGINE = os.getenv("DEFAULT_ENGINE") or "code-davinci-002"
DEFAULT_MESSAGE_PROMPT = os.getenv("DEFAULT_MESSAGE_PROMPT") or f"\"\"\"\n1. Write in {DEFAULT_LANGUAGE}: "
TESSERACT_CONFIG = os.getenv("TESSERACT_CONFIG") or "--psm 6"

# load open ai
def call_openai(engine, prompt):
    openai.api_key = OPENAI_APIKEY

    response = openai.Completion.create(
        engine=engine,
        prompt=prompt,
        temperature=0.9,
        max_tokens=1000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )
    return response["choices"][0]["text"]


# iterate through all images in the directory
# and concatenate all the text into a single string
def combine_images():
    # check if directory exist
    if not os.path.exists(DIRECTORY + "/images"):
        os.mkdir(DIRECTORY + "/images")


    for i in range(len(os.listdir(DIRECTORY + "/images"))):
        filename = f"{i}.png"
        f = os.path.join(DIRECTORY + "/images", filename)
        print(f)
        if os.path.exists(f):
            img = PIL.Image.open(f)
            pytesseract.tesseract_cmd = PATH_TO_TESSERACT
            result = pytesseract.image_to_string(img, config=TESSERACT_CONFIG)
            
            with open(DIRECTORY + "/problem.txt", "a") as file:
                file.write(result)

    return result
        
# call openai to generate code
def problem_processing():
    code_problem = DEFAULT_MESSAGE_PROMPT + open("problem.txt", "r").read() + "s\n\"\"\""
    code_solution = call_openai(DEFAULT_ENGINE, code_problem)

    print(code_solution)

    file_name = check_programming_language(default_lang=DEFAULT_LANGUAGE)

    with open(DIRECTORY + f"/{file_name}", "a") as file:
        file.write(code_solution)

def check_programming_language(default_lang):
    file_name = {
        "python": "solution.py",
        "javascript": "solution.js",
        "java": "solution.java",
        "c++": "solution.cpp",
        "c": "solution.c",
        "_": "solution.txt"
    }
    return file_name.get(default_lang, file_name["_"])

def check_file_exist(file):
    if os.path.exists(file):
        os.remove(file)
    
if __name__ == "__main__":
    print("Starting script...")
    # check if existing files
    check_file_exist(DIRECTORY + f"/{check_programming_language(default_lang=DEFAULT_LANGUAGE)}")
    # process images
    combine_images()
    # process problem
    problem_processing()
    # remove problem.txt
    check_file_exist(DIRECTORY + "/problem.txt")
    print("Script completed!")
