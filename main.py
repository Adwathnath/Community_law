from flask import Flask, render_template, jsonify, request, Response
from flask_pymongo import PyMongo
from openai import OpenAI
from DBConnection import *
from flask_cors import CORS
import time


app = Flask(__name__)
CORS(app)
app.config["MONGO_URI"] = "mongodb+srv://adwaithnathbablu333666:KtOxom7TyNi7YsXp@cluster0.eehtqrl.mongodb.net/communitylaw"
mongo = PyMongo(app)

client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

@app.route("/")
def homepage():
    return render_template("home.html")

@app.route("/login")
def login():
    return render_template("login.html")


@app.route('/logincode',methods=['post'])
def logincode():
    uname=request.form['typeEmailX']
    pswd=request.form['typePasswordX']
    qry="select * from register where email=%s and password=%s "
    val=(uname,pswd)
    res=selectone(qry,val)
    print(uname,pswd)
    print("response----",res)
    if res is None:
        return '''<script>alert("invalid username");
                window.location='/'</script>'''  

    else:
        chats = mongo.db.chats.find({})
        myChats = [chat for chat in chats]
        print(myChats)
        return render_template("index.html", myChats = myChats)
    

@app.route("/chat")
def home():
    chats = mongo.db.chats.find({})
    myChats = [chat for chat in chats]
    print(myChats)
    return render_template("index.html", myChats = myChats)

@app.route("/signup")
def signup():
    return render_template("registration.html")

@app.route('/cc_register_code',methods=['post'])
def cc_register_code():
    name = request.form['textfield']
    lname = request.form['textfield2']
    email = request.form['textfield3']
    password=request.form['textfield4']
    qry = "insert into register values(null ,%s,%s,%s,%s)"
    val=(name,lname,email,password)
    iud(qry,val)
    return '''<script>alert("Successfull");
                    window.location='/'</script>'''





@app.route("/help_html")
def helpfn():
    return render_template("help.html")

@app.route("/api", methods=["GET", "POST"])
def qa():
    if request.method == "POST":
        question = request.json.get("question")
        chat = mongo.db.chats.find_one({"question": question})
        if chat:
            data = {"question": question, "answer": f"{chat['answer']}"}
            return jsonify(data)    
        else:
            history = [
                {"role": "system", "content": "You are an intelligent assistant named Community law. You only provide well-reasoned answers that are both correct and helpful about kerala and indian local self government laws.If possible, give brief and fast answers almost all the time."},
                {"role": "user", "content": question},
            ]
                
            completion = client.chat.completions.create(
                    model="lmstudio-community/Meta-Llama-3-8B-Instruct-GGUF",
                    messages=history,
                    temperature=0.7,
                    stream=True,
                )

            response = ""
            for chunk in completion:
                if chunk.choices[0].delta.content:
                        response += chunk.choices[0].delta.content
            
            mongo.db.chats.insert_one({"question": question, "answer": response})
            data = {"question": question, "answer": response}
        return jsonify(data)
    
    data = {"result": "Invalid request"}
    return jsonify(data)
    

if __name__ == "__main__":
    app.run(debug=True)

