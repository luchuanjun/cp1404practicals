from flask import Flask, render_template, request
import wikipedia

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        search_term = request.form.get("search_term")
        try:
            summary = wikipedia.summary(search_term, sentences=2)
            return render_template("result.html", term=search_term, summary=summary)
        except wikipedia.exceptions.DisambiguationError as e:
            return render_template("result.html", term=search_term, summary=f"结果不明确，请选择更具体的关键词。可能指：{e.options[:5]}")
        except wikipedia.exceptions.PageError:
            return render_template("result.html", term=search_term, summary="未找到相关页面。请检查拼写。")
        except Exception as e:
            return render_template("result.html", term=search_term, summary=f"发生错误：{str(e)}")
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
