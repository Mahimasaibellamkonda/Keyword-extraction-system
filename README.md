# Keyword Extraction System

A web-based Natural Language Processing application that extracts important keywords from user-provided text based on word frequency and stop-word filtering.

## Features

* Extracts important keywords from text
* Removes common stop words
* Calculates keyword frequency
* Displays the most frequently occurring keywords
* Simple and responsive web interface
* Built using Flask and Python
* Uses basic NLP text-processing techniques

## Technologies Used

* Python
* Flask
* HTML5
* CSS3
* Regular Expressions
* Python Collections

## Project Structure

```text
Keyword-Extraction-System/
│
├── app.py
├── requirements.txt
├── README.md
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
```

## Installation

### 1. Open the project folder

Open a terminal inside the project directory.

### 2. Install the required package

```bash
pip install -r requirements.txt
```

## Running the Application

Run:

```bash
python app.py
```

The application will start at:

```text
http://127.0.0.1:5000
```

Open this address in a web browser.

## How It Works

1. The user enters a paragraph or document.
2. Flask receives the text from the web form.
3. The text is converted into individual words.
4. Common stop words are removed.
5. The frequency of the remaining words is calculated.
6. The most frequently occurring words are selected as keywords.
7. The keywords and their frequencies are displayed on the webpage.

## Example

### Input

```text
Natural Language Processing is a field of
Artificial Intelligence. Natural Language Processing
allows computers to understand human language.
```

### Example Output

```text
language       2
natural        2
processing     2
artificial     1
intelligence   1
computers      1
understand     1
human          1
```

## Applications

Keyword extraction can be used in:

* Search engines
* Document analysis
* News article processing
* Text summarization
* Information retrieval
* Content recommendation
* Academic document analysis
* Social media analysis

## Purpose

This project demonstrates how basic Natural Language Processing techniques can be used to identify important terms from a text document and present them through a web-based application.

## Author

B.E. CSE Student
