# fake-news-GUI-app
## Installation
##### Prerequisites
1. Requires `python 3.6` or newer version of python to run.
2. Install dependencies using:
   - Install all the libraries in `requirements.txt` using the following command. 
   > Note: All command must be run in the same directory as `requirements.txt` to be installed.
   ```
   pip install -r requirements.txt
   ```
   - OR run all the bellow commands.
   ```
   pip install sklearn
   pip install numpy
   pip install pandas
   pip install pillow
   pip install newspaper3k
   ```
## Running Code
- firstly, try running the `main.py` file. Window like this should appear. ![alt text](https://github.com/chinmay91797/fake-news-GUI-app/blob/main/images/blank_window.jpg)
- Enter the news `URL:` you want to predict. it should scrap the article into text box and predict the results. ![alt text](https://github.com/chinmay91797/fake-news-GUI-app/blob/main/images/predict_window.jpg)
- if the GUI does not show the results properly, you can try running non-GUI file `prediction.py` to see if model is working or not.
- if `prediction.py` has some errors try running `modeling.py` becuase the `model.pickle` file might not be compatable with your version of sklearnk, so it recreats that file.
