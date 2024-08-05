from flask import Flask, render_template_string
import os

app = Flask(__name__)

# Read the border color from the environment variable
border_color = os.getenv('CSVSERVER_BORDER', 'Black')

# Read and parse the input file (adjust the file path as needed)
input_file = '/app/inputFile'
with open(input_file, 'r') as f:
    entries = f.readlines()[:7]  # Only take the first 7 entries

# HTML template for rendering the page
html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Welcome</title>
    <style>
        .welcome-note {
            border: 2px solid {{ border_color }};
            padding: 10px;
            width: fit-content;
        }
    </style>
</head>
<body>
    <div class="welcome-note">
        <h1>Welcome</h1>
        <p>Entries:</p>
        <ul>
            {% for entry in entries %}
            <li>{{ entry }}</li>
            {% endfor %}
        </ul>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(html_template, entries=entries, border_color=border_color)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9393)

