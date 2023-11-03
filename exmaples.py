from utils import Compiler

compiler = Compiler()

code = """
#include <iostream>
using namespace std;
int main() {
    cout << "Hello, World!";
    return 0;
}
"""

context = compiler.run(code)

print(context.formatter(code))
