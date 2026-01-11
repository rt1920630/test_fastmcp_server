import random
from fastmcp import FastMCP
import json

mcp = FastMCP(name="Simple calculator and dice roller")

@mcp.tool
def roll_dice(sides: int = 1) -> list[int]:
    """Roll a dice with the given number of sides."""
    return [random.randint(1, 6) for _ in range(sides)]

@mcp.tool
def add_numbers(a: float, b: float) -> float:
    """Add two numbers together."""
    return a + b

@mcp.tool
def subtract_numbers(a: float, b: float) -> float:
    """Subtract two numbers."""
    return a - b        

@mcp.tool
def multiply_numbers(a: float, b: float) -> float:
    """Multiply two numbers."""
    return a * b
@mcp.tool
def divide_numbers(a: float, b: float) -> float:
    """Divide two numbers."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
@mcp.tool
def power_numbers(a: float, b: float) -> float:
    """Raise a to the power of b."""
    return a ** b
@mcp.tool
def add_numbers(a: float, b: float) -> float:
    """Add two numbers together."""
    return a + b

@mcp.tool("info://server")
def server_info() -> str:
    """Provide information about the available resources."""
    info = (
        "name: Simple calculator and dice roller\n" \
        "tools: roll_dice, add_numbers, subtract_numbers, multiply_numbers, divide_numbers, power_numbers\n" \
        "description: A simple server that can roll dice and perform basic arithmetic operations."
        "version: 1.0.0\n"

    )
    return json.dumps(info, indent=4)

if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8000)
