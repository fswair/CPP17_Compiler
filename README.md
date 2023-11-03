# CPP17_Compiler
It's GCC Compiler for C/C++ working on Telegram.

# Commands
* run - prefixes=[/, !]
  - !run std=cxx [code]
  - !run [code]
* help - prefixes=/
  - /help

# Example Input
* !run std=14 ```cpp
#include <iostream>

int main() {
    using namespace std;
    std::cout << "Hello, World!";
    return 0;
}
```
