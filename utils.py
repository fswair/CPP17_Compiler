from config import RAPID_API_KEY
from re import search

class OutputContext(object):
    terminal_output: str = ""
    memory: float = 0.0
    std: int = 17
    status: str = False

    def formatter(self, __code: str) -> str:
        return f"""**Code:**\n```cpp\n{__code}```\n**Output:**```txt\n{self.terminal_output}```\n**Memory Usage:** {self.memory} MiB\n**Standart**: 20{self.std}\n**Status**: {'Successfully compiled!' if self.status else "An error has occured."}"""

class Compiler(object):
    def __init__(self):
        ...

    def convert_bytes(self, size: int):
        if not size:
            return 0.0
        return float("%.4f" % (float(size) / (1024 * 1024)))

    def execute(self, __code: str, __std: int | str = 17):
        import requests

        url = "https://online-code-compiler.p.rapidapi.com/v1/"

        payload = {
            "language": f"cpp{__std}",
            "version": "latest",
            "code": __code,
            "input": None
        }
        headers = {
            "content-type": "application/json",
            "X-RapidAPI-Key": RAPID_API_KEY,
            "X-RapidAPI-Host": "online-code-compiler.p.rapidapi.com"
        }

        response = requests.post(url, json=payload, headers=headers)

        context = OutputContext()
        print(response.json())
        context.terminal_output = response.json()["output"]
        context.memory = self.convert_bytes(response.json()["memory"])
        context.std = int(__std)
        context.status = bool(not search("\w+\.cpp:\d+:\d+", context.terminal_output))

        return context

    def run(self, __code: str, __std: int | str = 17) -> OutputContext:
        return self.execute(__code, __std)
