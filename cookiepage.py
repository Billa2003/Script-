from flask import Flask, render_template_string, request

app = Flask(__name__)

# HTML content, same as the screenshot
html_content = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>✌️WARRIOUR RULEX MULTI COOKIE SERVER🌀</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-image: url('https://wallpapercave.com/wp/wp1834945.jpg');
            background-size: cover;
            color: white;
            text-align: center;
        }
        h1 {
            margin-top: 50px;
            color: yellow;
        }
        form {
            background-color: rgba(0, 0, 0, 0.7);
            padding: 20px;
            border-radius: 10px;
            display: inline-block;
            margin-top: 20px;
        }
        input[type="text"], input[type="file"], input[type="number"] {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            border: none;
            border-radius: 5px;
        }
        input[type="submit"] {
            padding: 10px 20px;
            background-color: yellow;
            border: none;
            color: black;
            border-radius: 5px;
            cursor: pointer;
        }
        input[type="submit"]:hover {
            background-color: orange;
        }
        .task {
            margin-top: 20px;
            padding: 10px;
            background-color: rgba(255, 255, 255, 0.2);
            border-radius: 5px;
        }
        .stop-button {
            background-color: red;
            padding: 5px 10px;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        .footer {
            margin-top: 50px;
            color: yellow;
        }
    </style>
</head>
<body>
    <h1>Wariour rulex</h1>
    <p>❣️😎Offline post server multi cookies🐧🔥</p>
    <form method="POST" enctype="multipart/form-data">
        <label for="cookies">Upload Cookies File</label>
        <input type="file" id="cookies" name="cookies">
        
        <label for="post_id">Post ID</label>
        <input type="text" id="post_id" name="post_id" required>

        <label for="interval">Time Interval (in seconds)</label>
        <input type="number" id="interval" name="interval" required>

        <label for="comments_file">Upload Comments File (TXT)</label>
        <input type="file" id="comments_file" name="comments_file">
        
        <input type="submit" value="Start Sending Comments">
    </form>

    {% if task_running %}
    <div class="task">
        <p>Running Tasks</p>
        <p>Post ID: {{ post_id }} | Time Interval: {{ interval }}s</p>
        <button class="stop-button">Stop</button>
    </div>
    {% endif %}
    
    <div class="footer">
        <p>Contact me on Facebook</p>
    </div>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    task_running = False
    post_id = ''
    interval = 0

    if request.method == 'POST':
        # Get form data
        cookies = request.files.get('cookies')
        post_id = request.form.get('post_id')
        interval = request.form.get('interval')
        comments_file = request.files.get('comments_file')

        # Simulate task running for now
        task_running = True

    return render_template_string(html_content, task_running=task_running, post_id=post_id, interval=interval)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)