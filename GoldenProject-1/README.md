# Plagiarism Checker

## Overview

The Plagiarism Checker is a Python application that compares two pieces of text to determine their similarity, which can help identify potential instances of plagiarism. It uses Natural Language Processing (NLP) techniques to preprocess the text and calculate a similarity score.

## Features

- **Load Text Files**: Import text files from your local file system.
- **Text Preprocessing**: Automatically tokenizes, removes stopwords, and lemmatizes text for accurate comparison.
- **Similarity Calculation**: Uses TF-IDF vectorization and cosine similarity to measure how similar the two texts are.
- **GUI**: Provides a user-friendly graphical interface built with Tkinter.

## Libraries Used

- **`tkinter`**: For creating the graphical user interface (GUI). Allows users to interact with the application through text boxes, buttons, and labels.
- **`nltk` (Natural Language Toolkit)**: For text preprocessing. Provides tools for tokenization, stopword removal, and lemmatization.
- **`scikit-learn`**: For text vectorization and similarity calculation. Utilizes TF-IDF vectorization and cosine similarity to measure text similarity.

## Installation

To run this project, you'll need to install the required Python libraries. You can install them using `pip`:

```bash
pip install nltk scikit-learn
```
Additionally, download the required NLTK resources by running the following Python commands:

```bash
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
```

### Usage
Run the Application: Start the application by running the plagiarism_checker.py script.

```bash
python plagiarism_checker.py
```
Load Text Files: Click on "Load Text 1" and "Load Text 2" buttons to import the text files you want to compare.

Compare Texts: Click on the "Compare" button to calculate the similarity between the two texts. The similarity score will be displayed as a percentage.

## Code Explanation
load_file(entry): Opens a file dialog to select a text file and loads its content into the specified Text widget.

preprocess_text(text): Tokenizes, removes stopwords, and lemmatizes the input text to prepare it for similarity comparison.

compute_similarity(): Computes the cosine similarity between the preprocessed texts using TF-IDF vectorization and updates the result label.


### Example
1: Open the application and load two text files.

2: Click "Compare" to get the similarity score between the two texts.

3: The result will be displayed in the label as a percentage.
