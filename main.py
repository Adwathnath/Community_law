from flask import Flask, render_template, jsonify, request
from flask_pymongo import PyMongo
from openai import OpenAI




app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://adwaithnathbablu333666:KtOxom7TyNi7YsXp@cluster0.eehtqrl.mongodb.net/communitylaw"
mongo = PyMongo(app)

client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")


@app.route("/")
def home():
    chats = mongo.db.chats.find({})
    myChats = [chat for chat in chats]
    print(myChats)
    return render_template("index.html", myChats = myChats)

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
                {"role": "system", "content": "You are an intelligent assistant named Community law. You only provide well-reasoned answers that are both correct and helpful about kerala and indian local self government laws."},
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
           
            data = {"question": question, "answer": response}
            mongo.db.chats.insert_one({"question": question, "answer": response})
        return jsonify(data)
    
    data = {"result": "Invalid request"}
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)

