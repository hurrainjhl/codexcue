import tkinter as tk
from tkinter import filedialog, messagebox
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk

# Download the required NLTK resources
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')


# Function to load a text file
def load_file(entry):
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            entry.delete(1.0, tk.END)
            entry.insert(tk.END, text)


# Function to preprocess text
def preprocess_text(text):
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(text.lower())
    lemmatizer = WordNetLemmatizer()

    filtered_text = [lemmatizer.lemmatize(w) for w in word_tokens if w.isalnum() and w not in stop_words]

    return " ".join(filtered_text)


# Function to compute similarity between texts
def compute_similarity():
    text1 = preprocess_text(text_entry1.get(1.0, tk.END))
    text2 = preprocess_text(text_entry2.get(1.0, tk.END))

    if not text1.strip() or not text2.strip():
        messagebox.showerror("Error", "Both text fields must be filled.")
        return

    # Vectorize the text using TF-IDF
    vectorizer = TfidfVectorizer().fit_transform([text1, text2])
    vectors = vectorizer.toarray()

    # Compute the cosine similarity
    similarity = cosine_similarity(vectors)[0][1]

    result_label.config(text=f"Plagiarism: {similarity * 100:.2f}%")


# Initialize the main window
app = tk.Tk()
app.title("Plagiarism Checker")
app.geometry("600x600")
app.configure(bg='#1f1f1f')

# Text Entry 1
text_entry1 = tk.Text(app, height=10, width=60, bg='#333', fg='#fff')
text_entry1.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Load Text 1 Button
load_button1 = tk.Button(app, text="Load Text 1", command=lambda: load_file(text_entry1), bg='#444', fg='#fff',
                         relief='flat', padx=10, pady=5)
load_button1.grid(row=1, column=0, padx=10, pady=10, ipadx=10, ipady=5)

# Text Entry 2
text_entry2 = tk.Text(app, height=10, width=60, bg='#333', fg='#fff')
text_entry2.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Load Text 2 Button
load_button2 = tk.Button(app, text="Load Text 2", command=lambda: load_file(text_entry2), bg='#444', fg='#fff',
                         relief='flat', padx=10, pady=5)
load_button2.grid(row=3, column=0, padx=10, pady=10, ipadx=10, ipady=5)

# Compare Button
compare_button = tk.Button(app, text="Compare", command=compute_similarity, bg='#555', fg='#fff', relief='flat',
                           padx=10, pady=5)
compare_button.grid(row=3, column=1, padx=10, pady=10, ipadx=10, ipady=5)

# Result Label
result_label = tk.Label(app, text="Plagiarism: N/A", bg='#1f1f1f', fg='#fff')
result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=20)

app.mainloop()
