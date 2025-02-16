from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import github_md_to_html.main as gh
from spotify_actions.main import SpotifyActions

app = Flask(__name__)
spa = SpotifyActions()

cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"

github_user = "sins621"
github_repo = "Obsidian-Notes"


@app.route("/gh/get_tree")
@cross_origin()
def get_tree():
    return jsonify(gh.get_tree(github_user, github_repo))


@app.route("/gh/get_file")
@cross_origin()
def get_file():
    url = request.args.get("url", None)
    path = request.args.get("path", None)
    return gh.get_file(github_user, github_repo, url, path)


@app.route("/spa/<fn>")
@cross_origin()
def spotify_action(fn):
    print(fn)
    if request.args:
        function_output = getattr(spa, fn)(request.args)
        return jsonify(function_output)
    else:
        function_output = getattr(spa, fn)()
        if function_output:
            return jsonify(function_output)


if __name__ == "__main__":
    app.run(port=2000)
