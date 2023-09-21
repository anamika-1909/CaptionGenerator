from flask import Flask, request, render_template
from quote import quote
# Flask constructor
app = Flask(__name__)  
 
captions=list()
@app.route('/', methods =["GET", "POST"])
def getword():
    global captions
    captions.clear()
    if request.method == "POST":
       # getting input with name = fname in HTML form
       keyword = request.form.get("keyword")
       result = quote(keyword, limit=100)
    #    cap=list()
       for i in result:
        x=i['quote']
        if(len(x)<150):
            captions.append(x)
       return getcap()
    return render_template("form.html",captions=captions)
 
@app.route('/data')
def getcap():
    return render_template("data.html",captions=captions)


if __name__=='__main__':
   app.run()


