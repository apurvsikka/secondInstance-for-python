import tkinter as tk
from tkinter import font
import subprocess
def highlight_syntax(event):
    text.tag_remove("keyword", "1.0", "end")
    keywords = [" print "," False ", " None ", " True ", " and ", " as ", " assert ", " async ", " await ", " break ", " class ", " continue ",
                " def ", " del ", " elif ", " else ", " except ", " finally ", " for ", " from ", " global ", " if ", " import ",
                " in ", " is ", " lambda ", " nonlocal ", " not ", " or ", " pass ", " raise ", " return ", " try ", " while ", " with ","def ",
                "yield"]
    for keyword in keywords:
        start = "1.0"
        while True:
            start = text.search(keyword, start, stopindex="end")
            if not start:
                break
            end = f"{start}+{len(keyword)}c"
            text.tag_add("keyword", start, end)
            start = end

def run_code():
    code = text.get("1.0", "end-1c")
    with open("temp.py", "w") as file:
        file.write(code)
    subprocess.run(["python", "temp.py"])
    subprocess.run(["rm", "temp.py"])

root = tk.Tk()
text = tk.Text(root)
text.pack()

text.bind("<KeyRelease>", highlight_syntax)

text.tag_configure("keyword", foreground="blue", font=font.Font(weight="bold"))

run_button = tk.Button(root, text="Run", command=run_code)
run_button.pack()

root.mainloop()