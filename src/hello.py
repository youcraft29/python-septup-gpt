def greet(name: str, emoji: bool = True) -> str:
    return f"Hola, {name} {'👋' if emoji else ''}"


if __name__ == "__main__":
    print(greet("Mundo", True))
