# Import pickle and Article scraping modules
import pickle
from newspaper import Article

# Defining scrap function
def link(url):
    url_i = Article(url="%s" % (url), language='en') 
    url_i.download()
    url_i.parse()
    return url_i.text

# Defining news predicting function using previous model
def fakenews(var):
  load_model=pickle.load(open('data/model.pickle','rb'))
  prediction=load_model.predict([var])
  prob=load_model.predict_proba([var])
  dictx={"prediction": prediction[0], "probability": prob[0][1]}
  return dictx

# Running in non-GUI console
if __name__=='__main__':
  Userinput=input("URL: ")
  para=link(Userinput)
  values=fakenews(para)
  print(para)
  print(values['prediction'])
  print(values['probability'])
