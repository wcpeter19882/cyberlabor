# Prompt Tuning

A systematic workflow for iteratively refining and optimizing prompts using Azure OpenAI API.

## Overview

This project provides a systematic workflow for prompt tuning through multiple iterations:
- Generate output with Azure OpenAI
- Validate against quality guidelines
- Refine prompts based on validation results
- Repeat for improved results

## Installation

1. **Prerequisites:**
   - Azure CLI logged in: `az login`
   - Python 3.8+
   - Enable Claude skills in VSCode (set `chat.useAgentSkills` to true in settings)

2. **Clone the repository:**
   ```bash
   git clone https://github.com/wcpeter19882/cyberlabor.git
   cd cyberlabor
   ```

3. **Configure environment:**
   Create a `.env` file in the project root with:
   ```
   AZURE_OPENAI_ENDPOINT=your_endpoint
   AZURE_OPENAI_DEPLOYMENT=your_deployment
   AZURE_OPENAI_API_VERSION=2024-02-15-preview
   ```

## Usage

### Quick Start

```bash
python llm_call.py \
    --system-prompt system_prompt.md \
    --user-prompt user_prompt.md \
    --output-file output/test.txt
```

## Files

- `system_prompt.md` - System prompt template (editable sections specified)
- `user_prompt.md` - User prompt (readonly)
- `guidelines.md` - Quality validation criteria
- `llm_call.py` - Azure OpenAI API script
- `requirements.txt` - Python dependencies

## Dependencies

- `azure-identity>=1.15.0` - Azure CLI credential support
- `openai>=1.12.0` - Azure OpenAI SDK
- `python-dotenv>=1.0.0` - Environment variable loading

## License

[Add license information if applicable]