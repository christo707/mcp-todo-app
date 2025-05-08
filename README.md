# MCP Todo App

A powerful Todo application built using FastMCP, enhanced with LLM agent capabilities powered by Ollama qemu2.5. This application provides an intelligent and efficient way to manage your tasks with natural language understanding and automated task processing.

## Features

- Create new todo items with titles and optional descriptions
- Retrieve all todos or specific todo items
- Update existing todos (title, description, completion status)
- Delete todo items
- In-memory storage for quick access
- RESTful API interface
- Natural language task creation and management
- Intelligent task categorization and prioritization
- Automated task scheduling and reminders
- Smart task completion suggestions
- Context-aware task organization
- Natural language queries for task information
- Automated task follow-ups and status updates

## Prerequisites

- Python 3.10 or higher
- FastMCP 2.2.10 or higher
- Ollama qemu2.5
- Docker (for running Ollama)

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

4. Set up Ollama:
```bash
# Pull the qemu2.5 model
ollama pull qemu2.5
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

The TODO MCP provides the following API endpoints:

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



## License

[Add your license information here]

## Contributing

[Add contribution guidelines here]
