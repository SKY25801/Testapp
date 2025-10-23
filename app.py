import inspect
from flask import Flask, request, jsonify, render_template
from tools.search_tool import search
from tools.calculator_tool import calculate
from tools.file_system_tool import list_files
from tools.create_file_tool import create_file

app = Flask(__name__)

class Agent:
    def __init__(self):
        self.tools = {
            "search": search,
            "calculate": calculate,
            "list_files": list_files,
            "create_file": create_file,
        }

    def run(self, command):
        parts = command.split()
        tool_name = parts[0]

        if tool_name not in self.tools:
            return f"Unknown tool: {tool_name}"

        tool_func = self.tools[tool_name]
        sig = inspect.signature(tool_func)
        params = list(sig.parameters.values())
        args = parts[1:]

        num_params = len(params)

        if num_params == 0:
            return tool_func()

        if num_params == 1:
            if not args:
                if params[0].default is not inspect.Parameter.empty:
                    return tool_func()
                else:
                    return f"Missing argument for {tool_name}"

            arg = " ".join(args)
            return tool_func(arg)

        if num_params == 2:
            if len(args) < 2:
                return f"Usage: {tool_name} <{params[0].name}> <{params[1].name}>"

            arg1 = args[0]
            arg2 = " ".join(args[1:])
            return tool_func(arg1, arg2)

        return f"Tool '{tool_name}' has a signature that is not supported by the agent."


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
