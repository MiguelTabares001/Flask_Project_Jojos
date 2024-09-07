from flask import Flask, render_template, request


from gemini_ai import generate_prompt, to_markdown
#from markupsafe import escape


app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        prompt = request.form['prompt']
        response = generate_prompt(prompt)
        response = to_markdown(response)
        return render_template('index.html', response=response)
    return render_template('index.html')
    

if __name__ == "__main__":
    app.run(debug=True)



 #response = generate_promt("Generame un Stand de jojo's con su respectivo nombre en ingles, habilidades (solo información del stand) en español")
    #return f"<p>, {escape(response)}</p>"
    #return render_template('index.html', response=response)



