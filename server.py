from mcp.server.fastmcp import FastMCP
from typing import List
import json
from datetime import datetime
import sys
from config import Config

# Initialize FastMCP server
mcp = FastMCP(name="todo-app",
              host=Config.Server.HOST,
              port=Config.Server.PORT,
              sse_path=Config.Server.SSE_PATH)

# In-memory storage for todos
todos = []

# Helper function to generate unique ID
def generate_id() -> str:
    return str(len(todos) + 1)

# Create a new todo
@mcp.tool("create_todo", description="Create a new todo item with a title and optional description")
def create_todo(title: str, description: str = "") -> tuple:
    try:
        if not title:
            return 400, {"error": "Title is required"}
        
        todo = {
            "id": generate_id(),
            "title": title,
            "description": description,
            "completed": False,
            "created_at": datetime.now().isoformat()
        }
        
        todos.append(todo)
        return 201, todo
    except Exception as e:
        return 500, {"error": str(e)}

# Get all todos
@mcp.tool("get_todos", description="Retrieve all todo items in the system")
def get_todos() -> tuple:
    return 200, todos

# Get a specific todo
@mcp.tool("get_todo", description="Retrieve a specific todo item by its ID")
def get_todo(todo_id: str) -> tuple:
    try:
        todo = next((t for t in todos if t["id"] == todo_id), None)
        if not todo:
            return 404, {"error": "Todo not found"}
        
        return 200, todo
    except Exception as e:
        return 500, {"error": str(e)}

# Update a todo
@mcp.tool("update_todo", description="Update an existing todo item's properties (title, description, or completion status)")
def update_todo(todo_id: str, title: str = None, description: str = None, completed: bool = None) -> tuple:
    try:
        todo = next((t for t in todos if t["id"] == todo_id), None)
        if not todo:
            return 404, {"error": "Todo not found"}
        
        # Update fields
        if title is not None:
            todo["title"] = title
        if description is not None:
            todo["description"] = description
        if completed is not None:
            todo["completed"] = completed
        
        return 200, todo
    except Exception as e:
        return 500, {"error": str(e)}

# Delete a todo
@mcp.tool("delete_todo", description="Delete a todo item by its ID")
def delete_todo(todo_id: str) -> tuple:
    try:
        global todos
        todo = next((t for t in todos if t["id"] == todo_id), None)
        if not todo:
            return 404, {"error": "Todo not found"}
        
        todos = [t for t in todos if t["id"] != todo_id]
        return 200, {"message": "Todo deleted successfully"}
    except Exception as e:
        return 500, {"error": str(e)}

if __name__ == "__main__":
    print("STARTING")
    if len(sys.argv) > 1 and sys.argv[1] == "dev":
        mcp.run()  # Run without transport for dev server
    else:
        mcp.run(transport=Config.Server.TRANSPORT)  # Run with stdio for direct execution
