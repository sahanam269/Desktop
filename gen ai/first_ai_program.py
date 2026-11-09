import ollama
response = ollama.generate(model ="llama 3.2 latest",prompt="explain how ai works in one line  ")
print(response)