from flask import Flask, send_from_directory
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'img'  # 将此处替换为你的图片文件夹路径

@app.route('/images/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)