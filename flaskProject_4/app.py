from flask import Flask, request
import requests
import os
import time
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor

app = Flask(__name__)

def download_image(url):
    response = requests.get(url)
    if response.status_code == 200:
        filename = url.split('/')[-1]
        with open(filename, 'wb') as f:
            f.write(response.content)
        return f"{filename} downloaded successfully."
    else:
        return f"Failed to download {url}."

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        urls = request.form.get('urls').split('\n')
        start_time = time.time()

        with ThreadPoolExecutor() as executor:
            results = list(executor.map(download_image, urls))

        total_time = time.time() - start_time

        return "Downloaded images:\n" + '\n'.join([f'{result}' for result in results]) + "\nTotal execution time: " + str(total_time) + " seconds"

    return '''
    <form method="post">
        <textarea name="urls" placeholder="Enter image URLs (one per line)"></textarea>
        <input type="submit" value="Download Images">
    </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)