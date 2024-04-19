<h1 align="center">Buffer Project</h1>

<p align="center">
  <a href="https://your-build-status-url.com"><img alt="Build Status" src="https://your-build-status-url.com/status.svg"></a>
  <a href="https://your-license-url.com"><img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-yellow.svg"></a>
</p>

## 🚀 Introduction

Hello, I'm John Bulla, a seasoned Python developer. Welcome to the Buffer Project. I've implemented a Buffer class that supports two policies for item extraction - FIFO (First In First Out) and LIFO (Last In First Out). This project showcases best practices in Python programming, including clean, efficient code and comprehensive documentation.

## 🛠️ Technologies Used

- **Python**: The Buffer class is implemented in Python, taking advantage of its dynamic typing and built-in data structures.
- **pytest**: Unit tests are written using pytest, a powerful testing framework in Python.
- **GitHub**: The project is hosted on GitHub, making it easy to track changes and collaborate with others.

## 🎯 Features

- 📥 **Insert**: Add items to the buffer with ease.
- 📤 **Extract**: Retrieve items from the buffer according to the policy you choose.
- 📏 **Size**: Quickly check the size of the buffer.
- 📜 **Last Item**: Get the last item in the buffer with a simple method call.
- 🔍 **Find**: Efficiently find a specific element in the buffer.
- 📄 **Show**: Display the contents of the buffer in a user-friendly format.

## 📖 Usage

```python
# Create a Buffer with FIFO policy
buffer = Buffer('FIFO')

# Insert items
buffer.insert(1)
buffer.insert(2)
buffer.insert(3)

# Extract an item
item = buffer.extract()
print(item)  # Outputs: 1

# Check the size of the buffer
print(buffer.size())  # Outputs: 2

# Get the last item in the buffer
print(buffer.last_item())  # Outputs: 3

# Find a specific element in the buffer
buffer.find_element(2)  # Outputs: This element is in the position 0

# Show the contents of the buffer
print(buffer.show())  # Outputs: 2, 3

📦 Installation
To use this project, you need to have Python installed on your machine. Follow these steps to set up your environment:

1. Create a virtual environment:
    python3 -m venv venv

If you have problems with installation, run sudo apt-get update and sudo apt install python3.8-venv.

2. Activate the virtual environment:
    source venv/bin/activate

3. Install the required packages:
    pip install -r requirements.txt

🤝 Contributing
Contributions, issues and feature requests are welcome! Feel free to check issues page. You can also take a look at the contributing guide.

📝 License
This project is MIT licensed.

```