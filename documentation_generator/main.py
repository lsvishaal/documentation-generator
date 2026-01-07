# |---------------------------------------------------------|
# |                                                         |
# |                 Give Feedback / Get Help                |
# | https://github.com/getbindu/Bindu/issues/new/choose    |
# |                                                         |
# |---------------------------------------------------------|
#
#  Thank you users! We ❤️ you! - 🌻

"""documentation-generator - A Bindu Agent.

This project hosts a README generator agent that:
- Accepts a GitHub repository URL or `owner/repo` name
- Fetches repository details and languages via GitHub tools
- Writes a generated README to the local filesystem
"""

import argparse
import asyncio
import json
import os
from pathlib import Path
from typing import Any

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.models.openrouter import OpenRouter
from agno.tools.github import GithubTools
from agno.tools.local_file_system import LocalFileSystemTools
from bindu.penguin.bindufy import bindufy
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

agent: Agent | None = None
model_name: str | None = None
model_provider: str | None = None
openai_api_key: str | None = None
openrouter_api_key: str | None = None
github_token: str | None = None
output_dir: str | None = None
_initialized = False
_init_lock = asyncio.Lock()


def load_config() -> dict:
    """Load agent configuration from project root."""
    # Get path to agent_config.json in project root
    config_path = Path(__file__).parent / "agent_config.json"

    with open(config_path) as f:
        return json.load(f)


async def initialize_agent() -> None:
    """Initialize the agent once."""
    global agent, model_name, model_provider, openai_api_key, openrouter_api_key, github_token, output_dir

    # Ensure model_name is always a string
    global model_name
    model_name = model_name or "openai/gpt-4o-mini"
    # Determine which model to use based on available keys
    if openrouter_api_key:
        model = OpenRouter(id=model_name)
        model_provider = "OpenRouter"
    else:
        model = OpenAIChat(id=model_name)
        model_provider = "OpenAI"

    agent = Agent(
        name="Readme Generator Agent",
        model=model,
        tools=[
            GithubTools(access_token=github_token) if github_token else GithubTools(),
            LocalFileSystemTools(target_directory=output_dir or "./output"),
        ],
        markdown=True,
        instructions=[
            "You are a readme generator agent.",
            "You will be given a repository URL or a repository name.",
            "If given a URL, extract `owner/repo` from it.",
            "Use `get_repository(repo_name=owner/repo)` to fetch repository details.",
            "Also call `get_repository_languages(repo_name=owner/repo)`.",
            "Write a useful README for an open source project: cloning, install, usage, dev, contributing.",
            "Add helpful badges (license, stars, forks, issues, release, CI if detected, repo size).",
            "Do not include a languages-used section in the README.",
            "Write the produced README to the local filesystem using the local file system tool.",
        ],
    )
    print(f"✅ Agent initialized with {model_provider} model")


async def run_agent(messages: list[dict[str, str]]) -> Any:
    """Run the agent with the given messages.

    Args:
        messages: List of message dicts with 'role' and 'content' keys

    Returns:
        Agent response
    """
    global agent
    if agent is None:
        raise RuntimeError("Agent is not initialized")
    return await agent.arun(messages)




async def handler(messages: list[dict[str, str]]) -> Any:
    """Handle incoming agent messages.

    Args:
        messages: List of message dicts with 'role' and 'content' keys
                  e.g., [{"role": "system", "content": "..."}, {"role": "user", "content": "..."}]

    Returns:
        Agent response (ManifestWorker will handle extraction)
    """

    global _initialized

    # Lazy initialization on first call (in bindufy's event loop)
    async with _init_lock:
        if not _initialized:
            print("🔧 Initializing agent...")
            await initialize_all()
            _initialized = True

    # Run the async agent
    return await run_agent(messages)



async def initialize_all() -> None:
    """Initialize the agent."""
    await initialize_agent()


def main():
    """Main entry point for the Readme Generator Agent."""
    global model_name, openai_api_key, openrouter_api_key, github_token, output_dir

    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Bindu README Generator Agent")
    parser.add_argument(
        "--model",
        type=str,
        default=os.getenv("MODEL_NAME", "openai/gpt-4o-mini"),
        help="Model ID (default: openai/gpt-4o-mini for OpenRouter, gpt-4o-mini for OpenAI, env: MODEL_NAME)",
    )

    parser.add_argument(
        "--openai-api-key",
        type=str,
        default=os.getenv("OPENAI_API_KEY"),
        help="OpenAI API key (env: OPENAI_API_KEY)",
    )
    parser.add_argument(
        "--openrouter-api-key",
        type=str,
        default=os.getenv("OPENROUTER_API_KEY"),
        help="OpenRouter API key (env: OPENROUTER_API_KEY) - takes precedence over OpenAI",
    )
    parser.add_argument(
        "--github-token",
        type=str,
        default=os.getenv("GITHUB_ACCESS_TOKEN"),
        help="GitHub access token (env: GITHUB_ACCESS_TOKEN)",
    )
    parser.add_argument(
        "--output-dir",
        type=str,
        default=os.getenv("OUTPUT_DIR", "./output"),
        help="Directory where generated README files are written (env: OUTPUT_DIR)",
    )
    args = parser.parse_args()

    # Set global model name and API keys
    model_name = args.model
    openai_api_key = args.openai_api_key
    openrouter_api_key = args.openrouter_api_key
    github_token = args.github_token
    output_dir = args.output_dir

    # Require at least one LLM provider
    if not openrouter_api_key and not openai_api_key:
        raise ValueError("Either OPENROUTER_API_KEY or OPENAI_API_KEY required")  # noqa: TRY003
    if not github_token:
        raise ValueError("GITHUB_ACCESS_TOKEN required")  # noqa: TRY003

    provider = "OpenRouter" if openrouter_api_key else "OpenAI"
    print(f"🤖 Using model: {model_name} ({provider})")
    print(f"📁 Output dir: {output_dir}")

    # Load configuration
    config = load_config()

    # Bindufy and start the agent server
    # Note: agent is initialized lazily on first request
    print("🚀 Starting Bindu agent server...")
    bindufy(config, handler)


# Bindufy and start the agent server
if __name__ == "__main__":
    main()
