import tkinter as tk
import joblib

model=joblib.load("model.pkl")
vectorizer=joblib.load("vectorizer.pkl")

def check():

    url=entry.get()

    url_data=vectorizer.transform([url])

    prediction=model.predict(url_data)

    if prediction[0]==1:
        result.config(text="⚠ Suspicious Website")
    else:
        result.config(text="✅ Safe Website")


window=tk.Tk()

window.title("Fake Website Detector")

label=tk.Label(window,text="Enter URL")
label.pack()

entry=tk.Entry(window,width=40)
entry.pack()

button=tk.Button(window,text="Check",command=check)
button.pack()

result=tk.Label(window,text="")
result.pack()

window.mainloop()