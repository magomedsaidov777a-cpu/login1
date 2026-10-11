from http.server import BaseHTTPRequestHandler
import json
import requests
import os

BOT_TOKEN = os.environ.get("BOT_TOKEN", "8630784152:AAGNXDv5RWyMjwTSMK76HqYeGdGom6uIgT8")
SITE_URL = "https://magomedch777.pythonanywhere.com"

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(length).decode('utf-8')
        try:
            update = json.loads(body)
            msg = update.get("message", {})
            chat_id = msg.get("chat", {}).get("id")
            text = msg.get("text", "")
            if chat_id and text == "/start":
                reply = f"Привет! Твой бонус 5000 рублей ждёт.\nЗабери здесь: {SITE_URL}"
                requests.get(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
             json={
                 "chat_id": chat_id,
                 "text": reply,
                 "reply_markup": {
                     "inline_keyboard": [[
                         {"text": "🎁 ЗАБРАТЬ БОНУС", "url": SITE_URL}
                     ]]
                 }
             })
        except Exception:
            pass
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"ok")
