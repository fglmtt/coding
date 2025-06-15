import argparse
import json
import os
import openai

CREDENTIALS = os.path.join(os.path.dirname(__file__), "credentials.json")


def load_credentials():
    try:
        with open(CREDENTIALS, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError(f"credentials file '{CREDENTIALS}' not found")
    except json.JSONDecodeError:
        raise ValueError(f"credentials file '{CREDENTIALS}' is not a valid json")


def parse_arguments():
    parser = argparse.ArgumentParser(description="OpenAI API Query Client")
    parser.add_argument(
        "--temperature", type=float, default=1.0, help="temperature parameter"
    )
    parser.add_argument("--top_p", type=float, default=1.0, help="top_p parameter")
    return parser.parse_args()


def main():
    credentials = load_credentials()
    args = parse_arguments()

    client = openai.OpenAI(api_key=credentials["api_key"])
    while True:
        try:
            prompt = input("enter prompt: ")
        except (EOFError, KeyboardInterrupt):
            print("\nexiting...")
            break
        if not prompt.strip():
            continue
        try:
            response = client.responses.create(
                model="gpt-4o",
                input=prompt,
                temperature=args.temperature,
                top_p=args.top_p,
            )
            print("output:", response.output_text)
        except openai.OpenAIError as e:
            print(f"API error: {e}")
        except Exception as e:
            print(f"unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
