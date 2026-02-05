---
name: prompt-tuning
description: Iteratively refine and optimize prompts using Azure OpenAI API. Use when the user wants to tune, improve, or refine prompts through multiple iterations, or when they mention prompt optimization, prompt engineering, or iterative prompt refinement.
---

# Prompt Tuning

Iteratively refine prompts by generating output, validating against guidelines, and improving prompts through multiple cycles.

## Prerequisites

1. Azure CLI logged in: `az login`
2. `.env` file at project root with Azure OpenAI configuration
3. Dependencies installed (see Installation section below)

## Installation

If the script fails with a missing package error, install dependencies:

```bash
pip install -r .claude/skills/prompttuning/requirements.txt
```

This installs:
- `azure-identity` - Azure CLI credential support
- `openai` - Azure OpenAI SDK
- `python-dotenv` - Environment variable loading

## Required Inputs

The user must provide paths to these files:

| Input | Description |
|-------|-------------|
| System Prompt | Text file containing the system prompt to tune (specify which sections can be modified) |
| User Prompt | Text file containing the user prompt (typically readonly) |
| Guidelines | Text file with output quality guidelines for validation |
| Output File | Path where generated output will be saved |
| Iterations | Number of tuning cycles (default: 5) |

## Workflow

**CRITICAL: This is a sequential, iterative process. Each iteration MUST complete before the next begins. Do NOT batch or parallelize iterations.**

### For EACH iteration (1 through N):

#### Step 1: Generate Output

Run the LLM call script:

```bash
python .claude/skills/prompttuning/llm_call.py \
    --system-prompt <system_prompt_file> \
    --user-prompt <user_prompt_file> \
    --output-file <output_file>
```

#### Step 2: Read and Validate Output

1. **Read the generated output file**
2. **Read the guidelines file**
3. **Validate as a senior designer:**
   - Check EACH guideline item against the output
   - Score each category (1-10)
   - Identify SPECIFIC gaps with examples from the output
   - Note what's working well
   - Calculate overall score

#### Step 3: Analyze and Refine Prompts

Based on validation results:

1. **Identify the biggest gaps** - What guidelines scored lowest?
2. **Determine root cause** - Why is the output failing this guideline?
3. **Formulate prompt changes** - What instruction would fix this?
4. **Update the system prompt** (only the sections user specified as editable)

**CRITICAL RULES for prompt refinement:**
- Prompts must NEVER be content-specific (no examples with real names, projects, etc.)
- Rules should describe PATTERNS, not instances
- Each refinement should target a specific validation gap
- Changes should be additive/incremental, not wholesale rewrites

#### Step 4: Loop to Next Iteration

After updating the prompt, RETURN TO STEP 1 with the modified prompt.

Do NOT proceed to the next iteration without:
- Generating new output with the updated prompt
- Validating that output
- Making further refinements if needed

### After All Iterations: Final Report

Provide a summary:
- Score progression (iteration 1 → N)
- Key prompt changes and their impact
- Remaining gaps
- Before/after comparison of key outputs

## Anti-Patterns (What NOT to Do)

❌ **DO NOT** run all iterations in a loop without validation between each
❌ **DO NOT** batch generate outputs for all iterations at once
❌ **DO NOT** make prompt changes without first validating the current output
❌ **DO NOT** add content-specific examples to prompts
❌ **DO NOT** skip reading the output file before validation

## Example Session

User provides:
- System prompt: `system_prompt.md` (editable section: `# Personalization`)
- User prompt: `user_prompt.md` (readonly)
- Guidelines: `guidelines.md`
- Output file: `output/iteration.txt`
- Iterations: 5

**Iteration 1:**
1. Run `llm_call.py` → generates `output/iteration.txt`
2. Read output → Read guidelines → Validate → Score: 42/60
3. Gap identified: "Passive content has too many names"
4. Update `# Personalization` section: Add stricter name minimization rule

**Iteration 2:**
1. Run `llm_call.py` with UPDATED prompt → new output
2. Read output → Validate → Score: 46/60 (↑4)
3. Gap identified: "Not enough 'you' usage"
4. Update prompt: Add required "you/your" usage rule

**Iteration 3:**
1. Run `llm_call.py` with UPDATED prompt → new output
2. Read output → Validate → Score: 49/60 (↑3)
3. ...continue...
5. Report final results

## Senior Designer Perspective

When validating, adopt the mindset of a senior designer:
- High standards for quality
- Focus on user experience and clarity
- Attention to consistency and polish
- Constructive but demanding feedback
- Solutions-oriented critique
