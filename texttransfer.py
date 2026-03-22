import tkinter as tk

root = tk.Tk()
root.title("Text Editor")

root.label = tk.Label(root, text="Write something below.")
root.label.pack()

root.text = tk.Text(root, width=50, height=10)
root.text.pack()
root.text.focus_set()

# Status label to show submission info
root.status = tk.Label(root, text="Press Ctrl+Enter to submit")
root.status.pack()

def submit_text(event=None):
	content = root.text.get("1.0", "end-1c")
	print("--Your message--")
	print(content)
	root.status.config(text="Submitted to terminal window")
	return "break"

# Bind Ctrl+Enter to submit; Enter alone inserts a newline
root.text.bind('<Control-Return>', submit_text)

root.mainloop()
