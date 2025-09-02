from flask import Flask, render_template, request, redirect, flash

app = Flask(__name__)
app.secret_key = "segredo123"  # necessário para mensagens flash

@app.route('/', methods=['GET', 'POST'])
def contato():
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        mensagem = request.form.get('mensagem')

        if not nome or not email or not mensagem:
            flash("Todos os campos são obrigatórios!", "error")
            return redirect('/')

        # Salvar no arquivo
        with open("submissions.txt", "a") as f:
            f.write(f"Nome: {nome}\nEmail: {email}\nMensagem: {mensagem}\n{'-'*40}\n")

        flash("Mensagem enviada com sucesso!", "success")
        return redirect('/')

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
