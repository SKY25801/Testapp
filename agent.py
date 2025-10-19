from tools.search_tool import search
from tools.calculator_tool import calculate
from tools.file_system_tool import list_files

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

if __name__ == "__main__":
    agent = Agent()
    while True:
        command = input("Enter command: ")
        if command.lower() == "exit":
            break
        result = agent.run(command)
        print(result)
