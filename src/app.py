from flask import Flask, render_template, request



app = Flask(__name__)

@app.route("/")
def index():
   # return "<h1>Hola mundo desde Flask!! mi porpio html</h1>"
    lengs = ["Python", "Java", "Kotlin", "#C", "JS","RUBY"]
    mydata = {
        "titulo": "pagina 1",
        "saludo": "welcome to the jungle mai friend",
        "cursos": lengs,
        "n_cursos": len(lengs)
    }

    return render_template("index.html", data = mydata)


def status_404(error):
    return "HOLA 404"
app.register_error_handler(404,status_404)

if __name__ == "__main__":
    app.run(debug=True)


