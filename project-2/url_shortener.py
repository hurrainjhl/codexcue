import tkinter as tk
from tkinter import messagebox, ttk
import pyshorteners
import webbrowser

# Function to shorten the URL using the selected service
def shorten_url():
    long_url = url_entry.get()
    service = service_combo.get().lower()

    if not long_url:
        messagebox.showerror("Error", "Please enter a URL")
        return

    try:
        s = pyshorteners.Shortener()
        if service == 'tinyurl':
            short_url = s.tinyurl.short(long_url)
        elif service == 'bitly':
            api_key = "YOUR_BITLY_API_KEY"  # Replace with your Bitly API key
            s = pyshorteners.Shortener(api_key=api_key)
            short_url = s.bitly.short(long_url)
        elif service == 'isgd':
            short_url = s.isgd.short(long_url)
        elif service == 'osdb':
            short_url = s.osdb.short(long_url)
        else:
            messagebox.showerror("Error", f"Service '{service}' is not supported")
            return

        result_entry.delete(0, tk.END)
        result_entry.insert(tk.END, short_url)
        open_in_browser_button.config(state=tk.NORMAL)
    except Exception as e:
        messagebox.showerror("Error", str(e))
        open_in_browser_button.config(state=tk.DISABLED)

# Function to open the shortened URL in a web browser
def open_in_browser():
    short_url = result_entry.get()
    if short_url:
        webbrowser.open(short_url)

# Initialize the main window
app = tk.Tk()
app.title("URL Shortener")

# URL Entry
tk.Label(app, text="Enter URL:").grid(row=0, column=0, padx=10, pady=10)
url_entry = tk.Entry(app, width=50)
url_entry.grid(row=0, column=1, padx=10, pady=10)

# Service Selection ComboBox
tk.Label(app, text="Select Service:").grid(row=1, column=0, padx=10, pady=10)
service_combo = ttk.Combobox(app, values=["TinyURL", "Bitly", "Isgd", "Osdb"])
service_combo.grid(row=1, column=1, padx=10, pady=10)
service_combo.current(0)  # Set default selection to TinyURL

# Shorten URL Button
shorten_button = tk.Button(app, text="Shorten URL", command=shorten_url)
shorten_button.grid(row=2, column=0, columnspan=2, pady=10)

# Result Entry
tk.Label(app, text="Short URL:").grid(row=3, column=0, padx=10, pady=10)
result_entry = tk.Entry(app, width=50)
result_entry.grid(row=3, column=1, padx=10, pady=10)

# Open in Browser Button
open_in_browser_button = tk.Button(app, text="Open in Browser", command=open_in_browser, state=tk.DISABLED)
open_in_browser_button.grid(row=4, column=0, columnspan=2, pady=10)

app.mainloop()
