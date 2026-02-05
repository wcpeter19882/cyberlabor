#!/usr/bin/env python3
"""
Azure OpenAI LLM Call Script

Simple script to call Azure OpenAI API with system and user prompts from files.
Uses Azure CLI credentials for authentication.
"""

import argparse
import os
import sys
from pathlib import Path

from dotenv import load_dotenv
from azure.identity import AzureCliCredential
from openai import AzureOpenAI

# Load .env file from project root
load_dotenv(Path(__file__).resolve().parents[3] / ".env")


def get_azure_openai_client() -> AzureOpenAI:
    """Initialize Azure OpenAI client with CLI credentials."""
    endpoint = os.environ.get("AZURE_OPENAI_ENDPOINT")
    if not endpoint:
        raise ValueError("AZURE_OPENAI_ENDPOINT environment variable is required")
    
    credential = AzureCliCredential()
    token = credential.get_token("https://cognitiveservices.azure.com/.default")
    
    api_version = os.environ.get("AZURE_OPENAI_API_VERSION", "2024-02-15-preview")
    
    client = AzureOpenAI(
        azure_endpoint=endpoint,
        api_key=token.token,
        api_version=api_version,
    )
    return client


def read_file(file_path: str) -> str:
    """Read content from a file."""
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read().strip()


def write_file(file_path: str, content: str) -> None:
    """Write content to a file."""
    Path(file_path).parent.mkdir(parents=True, exist_ok=True)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)


def call_llm(
    client: AzureOpenAI,
    deployment: str,
    system_prompt: str,
    user_prompt: str,
    temperature: float = 0.7,
    max_tokens: int = 4096,
) -> str:
    """Make a call to Azure OpenAI API."""
    response = client.chat.completions.create(
        model=deployment,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        temperature=temperature,
        max_completion_tokens=max_tokens,
    )
    return response.choices[0].message.content


def main():
    parser = argparse.ArgumentParser(
        description="Call Azure OpenAI API with system and user prompts from files"
    )
    parser.add_argument(
        "--system-prompt", "-s",
        required=True,
        help="Path to the system prompt text file"
    )
    parser.add_argument(
        "--user-prompt", "-u",
        required=True,
        help="Path to the user prompt text file"
    )
    parser.add_argument(
        "--content", "-c",
        help="Path to optional content file to append to user prompt"
    )
    parser.add_argument(
        "--output-file", "-o",
        required=True,
        help="Path to save the output response"
    )
    parser.add_argument(
        "--temperature", "-t",
        type=float,
        default=0.7,
        help="Sampling temperature (default: 0.7)"
    )
    parser.add_argument(
        "--max-tokens", "-m",
        type=int,
        default=4096,
        help="Maximum tokens in response (default: 4096)"
    )
    
    args = parser.parse_args()
    
    # Validate input files exist
    for file_path, name in [
        (args.system_prompt, "System prompt"),
        (args.user_prompt, "User prompt"),
    ]:
        if not os.path.exists(file_path):
            print(f"Error: {name} file not found: {file_path}", file=sys.stderr)
            sys.exit(1)
    
    if args.content and not os.path.exists(args.content):
        print(f"Error: Content file not found: {args.content}", file=sys.stderr)
        sys.exit(1)
    
    # Validate environment variables
    deployment = os.environ.get("AZURE_OPENAI_DEPLOYMENT")
    if not deployment:
        print("Error: AZURE_OPENAI_DEPLOYMENT environment variable is required", file=sys.stderr)
        sys.exit(1)
    
    # Initialize client
    print("Initializing Azure OpenAI client...")
    try:
        client = get_azure_openai_client()
    except Exception as e:
        print(f"Error: Failed to initialize client: {e}", file=sys.stderr)
        print("Make sure you are logged in with 'az login'", file=sys.stderr)
        sys.exit(1)
    
    # Load prompts
    system_prompt = read_file(args.system_prompt)
    user_prompt = read_file(args.user_prompt)
    
    # Append content if provided
    if args.content:
        content = read_file(args.content)
        user_prompt = f"{user_prompt}\n\n## Content\n{content}"
    
    print(f"System prompt: {len(system_prompt)} chars")
    print(f"User prompt: {len(user_prompt)} chars")
    
    # Call LLM
    print("Calling Azure OpenAI...")
    try:
        response = call_llm(
            client, deployment, system_prompt, user_prompt,
            args.temperature, args.max_tokens
        )
    except Exception as e:
        print(f"Error: LLM call failed: {e}", file=sys.stderr)
        sys.exit(1)
    
    # Save output
    write_file(args.output_file, response)
    print(f"Output saved to: {args.output_file}")
    print(f"Output length: {len(response)} chars")


if __name__ == "__main__":
    main()
