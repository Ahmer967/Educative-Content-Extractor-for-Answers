# Educative-Content-Extractor
Script written using Python and Selenium that automatically extracts the content of Answers on Educative platform into a text file.

## Important pointers
* When you run the script, you might receive an error that chromedriver is not trusted. Please follow the following link in order to fix this error: https://timonweb.com/misc/fixing-error-chromedriver-cannot-be-opened-because-the-developer-cannot-be-verified-unable-to-launch-the-chrome-browser-on-mac-os/
* Execution time and speed of the script depends on your internet connection!

## Running the script
**Note:** Replace `pip3` with `pip` in the commands below if the commands do not work with `pip3`
1) **Clone the repository:** `git clone https://github.com/Ahmer967/Educative-Content-Extractor-for-Answers.git`
2) **Navigate to the `Educative-Content-Extractor` directory:** `cd Educative-Content-Extractor-for-Answers`
3) **Install virtual environment (if not already installed):** `pip3 install virtualenv`
4) **Create virtual environment:** `python3 -m venv env`
5) **Enable virtual environment:** `source env/bin/activate`
6) **Upgrade `pip`:** `"env/bin/python3" -m pip install --upgrade pip`
7) **Install `wheel`:** `pip3 install wheel`
8) **Install required libraries and packages:** `pip3 install -r requirement.txt`
9) **Run program:** `python3 answer.py`

Follow the instructions on the terminal to successfully scrape the contents of the course into a text file. Contents will be written to `course.txt` file

## Format
* Answer title (h1 heading extracted into text file)
* Lesson content (contents of p tags of lessons extracted to text file)
* Now the contents of TOCs is extracted into the text file
* Now the contents of bullet points are extracted. These are bullet points in the form of `li` tags inside the lesson

## Limitations
* Content of code blocks, code widgets, SPA, etc are not extracted
* Latex will not be extracted
