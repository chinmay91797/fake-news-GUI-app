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

article_var='''The House is scheduled to take up and likely vote on the impeachment of President Donald Trump on Wednesday, bringing Congress one step closer to making history and impeaching a president for the second time during his tenure.

House Majority Leader Steny Hoyer of Maryland on Monday announced the schedule for the next two days and how the lower chamber will proceed with its attempts in trying to remove Trump , who is set to leave office in nine days. Democrats argue Trump should be held accountable for encouraging his supporters to stop the certification of the Electoral College vote, which later devolved into violents riots and a breach of the U.S. Capitol last week.

The House will first take up and vote Tuesday evening on Democratic Rep. Jamie Raskin of Maryland's legislation calling on Vice President Mike Pence and the Cabinet to invoke the 25th Amendment for Trump's immediate removal. GOP Rep. Alex Mooney of West Virginia objected to passing it through unanimous consent on Monday morning, but the bill is expected to pass Tuesday. House Speaker Nancy Pelosi of California is then giving Pence 24 hours to respond.

The Week in Cartoons: Jan. 11-15 View All 21 Images

Hoyer's office confirmed the House will convene at 9 a.m. Wednesday to consider the articles of impeachment. One article of impeachment, authored by Raskin, Rep. Ted Lieu of California and Rep. David Cicilline of Rhode Island, was introduced at Monday's pro-forma session and seeks to charge the outgoing president with the "incitement of insurrection." 

The resolution appears to have reached the necessary support to pass the Democratic-led House without any GOP co-sponsors. Only a simple majority is needed to impeach a president. But Republicans, some of whom have considered the removal of the president in the wake of the Capitol breach, could ultimately sign onto the effort. No House Republicans in late 2019 voted to impeach the president, and only one GOP senator, Mitt Romney of Utah, voted to convict Trump on one of the articles of impeachment.

The single article of impeachment warns that Trump remains "a national security threat" and calls for impeachment, removal from office "and disqualification to hold and enjoy any office of honor, trust or profit under the United States."

Questions remain over when exactly the Senate would hold a potential trial. Some Democrats have suggested delaying it until after the Jan. 20 inauguration of President-elect Joe Biden, but others in leadership, including Hoyer, want them transmitted to the Senate immediately, pending passage of the impeachment resolution in the House.

A two-thirds majority, or 67 senators, is needed to convict a president, which has never happened in U.S. history. It would be a tough threshold to reach in what is poised to soon become a 50-50 Senate, meaning 17 Republicans would need to vote in favor if Democrats were unified. So far, GOP Sen. Ben Sasse of Nebraska, a Trump critic, has said he'll consider any articles of impeachment the House sends over.

"Whether impeachment can pass the United States Senate is not the issue," Hoyer told reporters at the Capitol on Monday. "The issue is we have a president who most of us believe participated in encouraging an insurrection, an act on this building and on democracy and trying to subvert the counting of the presidential ballot."'''


# URL FRAME
frame_url=tk.Frame(root)
frame_url.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.1)

url_label=tk.Label(frame_url, text="URL:")
url_label.place(relx=0.01, rely=0.1, relwidth=0.08, relheight=0.8)

url_entry=tk.Entry(frame_url, fg='grey', font=(13))
url_entry.place(relx=0.10, rely=0.1, relwidth=0.7, relheight=0.8)

srh_btn=tk.Button(frame_url, relief='groove', text='Predict')
srh_btn.place(relx=0.81, rely=0.11, relwidth=0.18, relheight=0.78)


# ARTICLE FRAME
frame_article=tk.Frame(root)
frame_article.place(relx=0.05, rely=0.16, relwidth=0.9, relheight=0.63)

scroll=tk.Scrollbar(frame_article)
scroll.pack(side=RIGHT,fill=Y)

view_article=tk.Text(frame_article, yscrollcommand=scroll.set)
view_article.insert(tk.END, article_var)
view_article.pack(side=LEFT, fill=BOTH)
view_article.configure(state='disabled')

scroll.config(command=view_article.yview)


# PREDICTION FRAME
frame_pred=tk.Frame(root)
frame_pred.place(relx=0.05, rely=0.8, relwidth=0.9, relheight=0.15)

LabelPred=tk.Label(frame_pred, text='Prediction :')
LabelPred.place(relx=0,rely=0,relheight=0.45,relwidth=0.2)

LabelProb=tk.Label(frame_pred, text='Probability :')
LabelProb.place(relx=0,rely=0.5,relheight=0.45,relwidth=0.2)

ValuePred=tk.Text(frame_pred)
ValuePred.insert(tk.END, "FAKE")
ValuePred.place(relx=0.2,rely=0.05,relheight=0.35,relwidth=0.15)
ValuePred.configure(state='disabled')

ValueProb=tk.Text(frame_pred)
ValueProb.insert(tk.END, "69.7%")
ValueProb.place(relx=0.2,rely=0.55,relheight=0.35,relwidth=0.15)
ValueProb.configure(state='disabled')




root.mainloop()