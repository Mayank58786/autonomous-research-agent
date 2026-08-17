from app.config import OPENAI_API_KEY


def main():
    print("Configuration loaded successfully.")
    print(f"API key detected: {bool(OPENAI_API_KEY)}")


if __name__ == "__main__":
    main()