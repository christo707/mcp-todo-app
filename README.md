# MCP Todo App

A simple yet powerful Todo application built using FastMCP, providing a clean and efficient way to manage your tasks.

## Features

- Create new todo items with titles and optional descriptions
- Retrieve all todos or specific todo items
- Update existing todos (title, description, completion status)
- Delete todo items
- In-memory storage for quick access
- RESTful API interface

## Prerequisites

- Python 3.10 or higher
- FastMCP 2.2.10 or higher

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd mcp-todo-app
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
```

3. Install dependencies:
```bash
pip install -e .
```

## Running the Application

### Development Mode
To run the application in development mode:
```bash
python server.py dev
```

### Production Mode
To run the application in production mode:
```bash
python server.py
```

## API Endpoints

The application provides the following API endpoints:

- `create_todo`: Create a new todo item
  - Required: title
  - Optional: description

- `get_todos`: Retrieve all todo items

- `get_todo`: Retrieve a specific todo item
  - Required: todo_id

- `update_todo`: Update an existing todo item
  - Required: todo_id
  - Optional: title, description, completed

- `delete_todo`: Delete a todo item
  - Required: todo_id

## Project Structure

- `server.py`: Main server implementation with API endpoints
- `client.py`: Client implementation for interacting with the server
- `config.py`: Configuration settings
- `main.py`: Entry point for the application

## License

[Add your license information here]

## Contributing

[Add contribution guidelines here]
