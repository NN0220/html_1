from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def profile():
    user_info = {
        "name": "Nnn",
        "title": "114590053",
        "bio": "a",
        "skills": ["Python", "HTML", "CSS", "Git"],
        "email": "t114590053@ntut.org.tw",
    }
    return render_template("2026_11_25.html", user=user_info)


if __name__ == "__main__":
    app.run(debug=True)