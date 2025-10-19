from flask import Flask, request, jsonify, render_template
from tools.search_tool import search
from tools.calculator_tool import calculate
from tools.file_system_tool import list_files

app = Flask(__name__)

class Agent:
    def __init__(self):
        self.tools = {
            "search": search,
            "calculate": calculate,
            "list_files": list_files,
        }

    def run(self, command):
        parts = command.split()
        tool_name = parts[0]
        if tool_name in self.tools:
            arg = " ".join(parts[1:])
            if tool_name == "list_files" and not arg:
                return self.tools[tool_name]()
            return self.tools[tool_name](arg)
        else:
            return f"Unknown tool: {tool_name}"

agent = Agent()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/agent", methods=["POST"])
def run_agent():
    command = request.json.get("command")
    if not command:
        return jsonify({"error": "Command not provided"}), 400
    result = agent.run(command)
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)
