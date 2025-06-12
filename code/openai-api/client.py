import argparse
import json
import openai

CREDENTIALS = "credentials.json"


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
    parser.add_argument("--prompt", type=str, required=True, help="prompt")
    parser.add_argument(
        "--temperature", type=float, default=1.0, help="temperature parameter"
    )
    parser.add_argument("--top_p", type=float, default=1.0, help="top_p parameter")
    return parser.parse_args()


def main():
    credentials = load_credentials()
    args = parse_arguments()

    client = openai.OpenAI(api_key=credentials["api_key"])
    print("prompt:", args.prompt)
    response = client.responses.create(
        model="gpt-4o",
        input=args.prompt,
        temperature=args.temperature,
        top_p=args.top_p,
    )
    print("output:", response.output_text)


if __name__ == "__main__":
    main()
