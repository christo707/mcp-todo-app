
import asyncio
from mcp import ClientSession
from mcp.client.stdio import stdio_client
from mcp import StdioServerParameters
from config import server_url

async def run_client_session():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
        env=None
    )

    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            result = await session.list_tools()
            print("\nAvailable Tools:")
            for tool in result.tools:
                print(f"- {tool.name}")

            # while True:
            #     user_input = input("\nEnter tool name (or 'exit' to quit): ")
            #     if user_input.lower() == 'exit':
            #         break
            #     if user_input in result.tools:
            #         arguments = {}
            #         # Assuming tools take simple string arguments for demonstration
            #         arg_input = input(f"Enter arguments for {user_input} (comma-separated key=value pairs): ")
            #         if arg_input:
            #             for item in arg_input.split(','):
            #                 key, value = item.split('=')
            #                 arguments[key.strip()] = value.strip()
                    
            #         result = await session.call_tool(user_input, arguments=arguments)
            #         print("Result:", result)
            #     else:
            #         print("Invalid tool name.")

if __name__ == "__main__":
    asyncio.run(run_client_session())