from typing import ValuesView
from newspaper import article
import prediction
import tkinter as tk
from tkinter.constants import BOTH, FLAT, GROOVE, LEFT, RIGHT, Y


root=tk.Tk()
root.geometry("600x400")
root.resizable(0,0)
root.update_idletasks()
width = root.winfo_width()
frm_width = root.winfo_rootx() - root.winfo_x()
win_width = width + 2 * frm_width
height = root.winfo_height()
titlebar_height = root.winfo_rooty() - root.winfo_y()
win_height = height + titlebar_height + frm_width
x = root.winfo_screenwidth() // 2 - win_width // 2
y = root.winfo_screenheight() // 2 - win_height // 2
root.geometry('{}x{}+{}+{}'.format(width, height, x, y))
root.deiconify()

url_var=tk.StringVar()


# URL FRAME
frame_url=tk.Frame(root)
frame_url.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.1)
# ARTICLE FRAME
frame_article=tk.Frame(root)
frame_article.place(relx=0.05, rely=0.16, relwidth=0.9, relheight=0.63)
# PREDICTION FRAME
frame_pred=tk.Frame(root)
frame_pred.place(relx=0.05, rely=0.8, relwidth=0.9, relheight=0.15)

url_label=tk.Label(frame_url, text="URL:")
url_label.place(relx=0.01, rely=0.1, relwidth=0.08, relheight=0.8)

url_entry=tk.Entry(frame_url, fg='grey', font=(13),textvariable=url_var)
url_entry.place(relx=0.10, rely=0.1, relwidth=0.7, relheight=0.8)

LabelPred=tk.Label(frame_pred, text='Prediction :')
LabelPred.place(relx=0,rely=0,relheight=0.45,relwidth=0.2)

LabelProb=tk.Label(frame_pred, text='Probability :')
LabelProb.place(relx=0,rely=0.5,relheight=0.45,relwidth=0.2)

scroll=tk.Scrollbar(frame_article)
scroll.pack(side=RIGHT,fill=Y)

def predict(entry):
    try:
        para=prediction.link(entry)
        values=prediction.fakenews(para)

        view_article=tk.Text(frame_article, yscrollcommand=scroll.set)
        view_article.insert(tk.INSERT, para)
        view_article.pack(side=LEFT, fill=BOTH)
        view_article.configure(state='disabled')
        scroll.config(command=view_article.yview)

        ValuePred=tk.Text(frame_pred)
        ValuePred.insert(tk.INSERT, values['prediction'])
        ValuePred.place(relx=0.2,rely=0.05,relheight=0.35,relwidth=0.15)
        ValuePred.configure(state='disabled')

        ValueProb=tk.Text(frame_pred)
        ValueProb.insert(tk.INSERT, values['probability'])
        ValueProb.place(relx=0.2,rely=0.55,relheight=0.35,relwidth=0.15)
        ValueProb.configure(state='disabled')

    except:
        values={'probability':'','prediction':'','paragraph':''}
        view_article=tk.Text(frame_article, yscrollcommand=scroll.set)
        view_article.insert(tk.INSERT, values['paragraph'])
        view_article.pack(side=LEFT, fill=BOTH)
        view_article.configure(state='disabled')
        scroll.config(command=view_article.yview)

        ValuePred=tk.Text(frame_pred)
        ValuePred.insert(tk.INSERT, values['prediction'])
        ValuePred.place(relx=0.2,rely=0.05,relheight=0.35,relwidth=0.15)
        ValuePred.configure(state='disabled')

        ValueProb=tk.Text(frame_pred)
        ValueProb.insert(tk.INSERT, values['probability'])
        ValueProb.place(relx=0.2,rely=0.55,relheight=0.35,relwidth=0.15)
        ValueProb.configure(state='disabled')

srh_btn=tk.Button(frame_url, relief='groove', text='Predict', command=lambda : predict(url_var.get()))
srh_btn.place(relx=0.81, rely=0.11, relwidth=0.18, relheight=0.78)


root.mainloop()