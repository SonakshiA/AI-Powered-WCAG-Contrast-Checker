from flask import Flask, render_template, request
from main import is_normal_text_compliant, is_large_text_compliant, is_ui_components_compliant
from Hugging_Face import recommend_foreground_color

app = Flask(__name__)
fg_color = ""
bg_color = ""
global results

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/submit",methods=['POST'])
def check_compliance():
    if request.method=='POST':
        fg_color = request.form['foreground']
        bg_color = request.form['background']
        print(fg_color,bg_color)
        results = {
                'is_normal_text_compliant':is_normal_text_compliant(fg_color,bg_color),
                'is_large_text_compliant':is_large_text_compliant(fg_color,bg_color),
                'is_ui_components_compliant':is_ui_components_compliant(fg_color,bg_color),
                'llm_response':recommend_foreground_color(bg_color)
            }
        return render_template("result.html",results=results)

@app.route('/submission',methods=['post'])
def get_ai_recommendations():
    response = recommend_foreground_color(bg_color)
    print("IS IT THIS: " , response)
    print(bg_color)
    new_results = {
                'is_normal_text_compliant':is_normal_text_compliant(fg_color,bg_color),
                'is_large_text_compliant':is_large_text_compliant(fg_color,bg_color),
                'is_ui_components_compliant':is_ui_components_compliant(fg_color,bg_color)
            }
    return render_template("test.html",results=new_results)

if __name__=="__main__":
    app.run(debug=True)