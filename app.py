from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)
# slack_name=maryam&track=backend

@app.route('/api', methods=['GET'])
def get_info():
    # Get query parameters
    slack_name = request.args.get("slack_name")
    track = request.args.get("track")

    # Get the current day and time of the week
    current_day = datetime.datetime.now().strftime('%A')

    current_utc_time = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

    # Get GitHub URLs
    github_repo_url = 'https://github.com/ayoblvck/backend_projs'
    github_file_url = 'https://github.com/ayoblvck/backend_projs/blob/main/app.py'

    # response JSON
    response_data = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": current_utc_time,
        "track": track,
        "github_file_url": github_file_url,
        "github_repo_url": github_repo_url,
        "status_code": 200
    }

    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)
