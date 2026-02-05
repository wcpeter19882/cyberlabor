## Overview

This project provides a claude skill for prompt tuning through multiple iterations:
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

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment:**
   Create a `.env` file in the project root with:
   ```
   AZURE_OPENAI_ENDPOINT=your_endpoint
   AZURE_OPENAI_DEPLOYMENT=your_deployment
   AZURE_OPENAI_API_VERSION=2024-02-15-preview
   ```

### Sample Skill Usage

Use this skill in Claude within VSCode by asking:

> "Help me refine my prompt. I have a system prompt in `system_prompt.md`, a user scenario in `user_prompt.md`, and quality criteria in `guidelines.md`.
> You can update "# Personalization" section in system_prompt.md, user_prompt.md is readonly.
> Run for 10 iterations
