---
name: prompt-tuning
description: Iteratively refine and optimize prompts using Azure OpenAI API. Use when the user wants to tune, improve, or refine prompts through multiple iterations, or when they mention prompt optimization, prompt engineering, or iterative prompt refinement.
---

# Prompt Tuning

Iteratively refine prompts by generating output, validating against guidelines, and improving prompts through multiple cycles.

## Prerequisites

1. Azure CLI logged in: `az login`
2. `.env` file at project root with Azure OpenAI configuration
3. Dependencies installed: `pip install -r .claude/skills/prompttuning/requirements.txt`

## Required Inputs

The user must provide paths to these files:

| Input | Description |
|-------|-------------|
| System Prompt | Text file containing the system prompt to tune |
| User Prompt | Text file containing the user prompt to tune |
| Content | Text file with content to process (used for testing prompts) |
| Guidelines | Text file with output quality guidelines for validation |
| Output File | Path where generated output will be saved |
| Iterations | Number of tuning cycles (default: 5) |

## Workflow

For each iteration, follow these steps:

### Step 1: Generate Output

Run the LLM call script to generate output with current prompts:

```bash
python .claude/skills/prompttuning/llm_call.py \
    --system-prompt <system_prompt_file> \
    --user-prompt <user_prompt_file> \
    --content <content_file> \
    --output-file <output_file>
```

### Step 2: Validate Output

Read the output file and the user-provided guidelines file:
- Output: Read from `<output_file>`
- Guidelines: Read from user-provided `<guidelines_file>`

Validate the output against EVERY guideline as a **senior designer**:
- Be critical and thorough
- Check each checkbox item in the guidelines
- Score each category 1-10
- Identify specific gaps and issues
- Note what works well

### Step 3: Refine Prompts

Based on validation results, update the system and/or user prompt files.

**CRITICAL RULES for prompt refinement:**
- Prompts must NEVER be content-specific
- Improve structure, clarity, and instructions
- Add constraints that help meet guidelines
- Prompts should work for ANY content in the domain
- Focus on HOW to process, not WHAT to process

### Step 4: Iterate

Repeat Steps 1-3 for the specified number of iterations (default: 5).

Track progress across iterations:
- Note which guidelines improved
- Note which guidelines still need work
- Observe patterns in what prompt changes are effective

### Step 5: Final Report

After all iterations, provide a summary:
- Starting vs ending guideline scores
- Key prompt changes that improved quality
- Remaining gaps (if any)
- Final refined prompts

## Example Session

User provides:
- System prompt: `prompts/system.txt`
- User prompt: `prompts/user.txt`  
- Content: `content/article.txt`
- Guidelines: `guidelines/quality.txt`
- Output file: `output/result.txt`
- Iterations: 3

Execution:
1. Run `llm_call.py` → read `output/result.txt`
2. Read `guidelines/quality.txt` → validate output → identify issues
3. Update `prompts/system.txt` and/or `prompts/user.txt`
4. Repeat 2 more times
5. Report final results

## Senior Designer Perspective

When validating, adopt the mindset of a senior designer:
- High standards for quality
- Focus on user experience and clarity
- Attention to consistency and polish
- Constructive but demanding feedback
- Solutions-oriented critique
