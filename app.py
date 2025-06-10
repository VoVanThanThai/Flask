from flask import Flask
import os

# Khởi tạo ứng dụng Flask
app = Flask(__name__)

# Cấu hình biến môi trường
PORT = int(os.environ.get('PORT', 10000))
HOST = '0.0.0.0'

# Dữ liệu mẫu
USER_DATA = {
    "name": "Võ Văn Thần Thái",
    "message": "Chào mừng bạn đến với ứng dụng của tôi!"
}

# Route chính trả về HTML trực tiếp
@app.route('/')
def home():
    html_content = f"""
    <!DOCTYPE html>
    <html lang="vi">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Chào mừng - {USER_DATA['name']}</title>
        <style>
            body {{
                margin: 0;
                font-family: 'Arial', sans-serif;
                height: 100vh;
                background: linear-gradient(135deg, #40E0D0 0%, #FF6B6B 100%);
                background-size: cover;
                display: flex;
                justify-content: center;
                align-items: center;
                color: #fff;
                text-align: center;
                overflow: hidden;
            }}
            .content {{
                background: rgba(255, 255, 255, 0.1);
                padding: 20px 40px;
                border-radius: 15px;
                backdrop-filter: blur(10px);
                box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
            }}
            h1 {{
                font-size: 48px;
                margin-bottom: 10px;
                text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
            }}
            p {{
                font-size: 24px;
                margin: 0;
            }}
            @keyframes moveBackground {{
                0% {{ background-position: 0% 50%; }}
                50% {{ background-position: 100% 50%; }}
                100% {{ background-position: 0% 50%; }}
            }}
            body {{
                animation: moveBackground 15s ease infinite;
            }}
        </style>
    </head>
    <body>
        <div class="content">
            <h1>Xin chào, {USER_DATA['name']}!</h1>
            <p>{USER_DATA['message']}</p>
        </div>
    </body>
    </html>
    """
    return html_content

# Route trạng thái (JSON)
@app.route('/status')
def status():
    return {"status": "online", "timestamp": "2025-06-10 21:24 +07"}

if __name__ == "__main__":
    app.run(host=HOST, port=PORT, debug=False)
