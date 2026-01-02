# 📘 Prompt Architect Agent - Usage Guide

## Table of Contents
1. [Quick Start](#quick-start)
2. [Core Concepts](#core-concepts)
3. [Using the Streamlit Interface](#using-the-streamlit-interface)
4. [Python API Usage](#python-api-usage)
5. [Template Library](#template-library)
6. [Advanced Features](#advanced-features)
7. [Best Practices](#best-practices)
8. [Examples](#examples)

---

## Quick Start

### Installation
```bash
# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app.py
```

### First Prompt Generation
1. Open the app in your browser (usually http://localhost:8501)
2. Type your idea: "Create a blog post about AI for beginners"
3. Click "Generate Structured Prompt"
4. Copy the generated prompt and use it with your LLM!

---

## Core Concepts

### What is Prompt Architect Agent?

Prompt Architect Agent automatically transforms brief, unstructured ideas into comprehensive, optimized prompts for Large Language Models. It extracts context, defines roles, structures instructions, and ensures quality—all without requiring prompt engineering expertise.

### Key Components

1. **Context Extraction**: Automatically detects intent, audience, tone, and format
2. **Role Definition**: Creates appropriate AI persona for the task
3. **Structured Instructions**: Generates layered, hierarchical guidance
4. **Constraints**: Adds quality assurance and LLM-specific optimizations
5. **Quality Criteria**: Defines evaluation standards for output

### Supported Categories

- **Content Creation**: Blogs, articles, marketing copy
- **Agent Development**: Chatbots, assistants, AI systems
- **Educational**: Tutorials, courses, explanations
- **Business**: Strategies, proposals, plans
- **Technical**: Code, documentation, debugging
- **Creative**: Stories, narratives, fiction
- **Analysis**: Data analysis, research, reports
- **Conversation**: Dialogue systems, chat interfaces

---

## Using the Streamlit Interface

### Main Interface

#### 1. Configuration (Sidebar)
- **Target LLM**: Select which LLM you're optimizing for
  - Claude 3.5 Sonnet (recommended for detailed reasoning)
  - Claude 3.5 Haiku (faster, more concise)
  - GPT-4 Turbo (balanced creativity and accuracy)
  - GPT-4o (latest GPT-4 variant)
  - Gemini Pro (Google's multimodal model)

#### 2. Advanced Options
- **Show Extracted Context**: Display detected intent, tone, audience, etc.
- **Show Prompt Components**: Break down role, instructions, constraints
- **Enable Copy Buttons**: Add copy-friendly code blocks

#### 3. Quick Examples
Load pre-built examples to see how the system works:
- Content Creation
- Agent Development
- Educational
- Business
- Technical

### Input Section

Simply type your idea in plain language. Examples:
- "Write a blog post about sustainable living"
- "Create a chatbot for customer support"
- "Explain quantum physics to teenagers"
- "Analyze sales data and find trends"

**No prompt engineering knowledge required!**

### Output Sections

#### Extracted Context
Shows what the system detected:
- **Intent**: What you want to do (create, analyze, explain, etc.)
- **Category**: Type of task (content, technical, educational, etc.)
- **Audience**: Who it's for (beginners, experts, general public, etc.)
- **Tone**: Communication style (professional, casual, academic, etc.)
- **Output Format**: Desired format (markdown, code, list, etc.)
- **Complexity**: Difficulty level (basic, intermediate, advanced)
- **Keywords**: Important terms extracted from your input

#### Prompt Components
Detailed breakdown:
- **Role Definition**: AI persona and expertise
- **Instructions**: Step-by-step guidance
- **Constraints**: Quality and style requirements
- **Quality Criteria**: Evaluation standards

#### Complete Structured Prompt
The final, ready-to-use prompt with all components assembled. You can:
- Copy directly to clipboard
- Download as Markdown file
- Export as JSON for programmatic use

---

## Python API Usage

### Basic Usage

```python
from prompt_architect import create_architect

# Create architect instance
architect = create_architect(target_llm="claude-3.5-sonnet")

# Transform raw input
raw_input = "Write a blog post about AI ethics for beginners"
result = architect.transform(raw_input)

# Use the generated prompt
print(result.full_prompt)
```

### Accessing Components

```python
# Get individual components
print("Role:", result.role_definition)
print("Instructions:", result.instructions)
print("Constraints:", result.constraints)
print("Quality Criteria:", result.quality_criteria)
```

### Context Extraction Only

```python
# Extract context without generating full prompt
context = architect.extract_context(raw_input)

print(f"Intent: {context.intent}")
print(f"Category: {context.category.value}")
print(f"Audience: {context.target_audience}")
print(f"Tone: {context.tone}")
print(f"Keywords: {context.keywords}")
```

### Different LLM Targets

```python
# Optimize for different LLMs
claude_architect = create_architect("claude-3.5-sonnet")
gpt_architect = create_architect("gpt-4-turbo")
gemini_architect = create_architect("gemini-pro")

# Each generates LLM-specific optimizations
claude_result = claude_architect.transform(raw_input)
gpt_result = gpt_architect.transform(raw_input)
gemini_result = gemini_architect.transform(raw_input)
```

---

## Template Library

### Using Pre-built Templates

```python
from prompt_templates import template_library

# List all templates
templates = template_library.list_templates()
print(templates)
# ['blog_post', 'chatbot_agent', 'tutorial_creator', ...]

# Get a specific template
template = template_library.get_template("blog_post")
print(template.name)
print(template.description)
print(template.variables)
```

### Filling Templates

```python
# Define values for template variables
values = {
    "topic": "artificial intelligence in healthcare",
    "audience": "healthcare professionals",
    "num_sections": "5",
    "tone": "professional yet accessible",
    "word_count": "1500"
}

# Fill template
filled_prompt = template_library.fill_template("blog_post", values)
print(filled_prompt)
```

### Available Templates

1. **blog_post**: Blog Post Writer
   - Variables: topic, audience, num_sections, tone, word_count

2. **chatbot_agent**: Chatbot Agent Developer
   - Variables: use_case, target_users, purpose, personality, capabilities, tone

3. **tutorial_creator**: Tutorial Creator
   - Variables: subject_area, topic, learner_level, learning_objectives

4. **business_strategy**: Business Strategy Developer
   - Variables: industry, strategy_type, business_description, target_market, current_situation, goals, timeline

5. **code_generator**: Code Generator
   - Variables: programming_language, domain, code_type, functionality, requirements, coding_standard

6. **data_analyst**: Data Analysis Expert
   - Variables: analysis_domain, data_description, analysis_focus, data_source, key_questions, analysis_type, deliverables, audience

7. **story_writer**: Creative Story Writer
   - Variables: genre, story_type, premise, setting, characters, tone, length, audience

### Browsing by Category

```python
# Get all templates in a category
educational_templates = template_library.get_templates_by_category("Educational")

for template in educational_templates:
    print(f"{template.name}: {template.description}")
```

---

## Advanced Features

### Custom Context Extraction

You can customize how context is extracted by modifying `prompt_architect.py`:

```python
# Add custom intent keywords
def _load_intent_keywords(self):
    return {
        "create": ["create", "generate", "write", "make"],
        "analyze": ["analyze", "examine", "evaluate"],
        # Add your custom intents here
        "custom_intent": ["custom", "keywords"],
    }
```

### Custom Role Definitions

Modify role generation logic:

```python
def generate_role_definition(self, context):
    # Add custom role logic
    if "custom_keyword" in context.keywords:
        return "You are a specialized expert in..."
    # Default behavior
    return super().generate_role_definition(context)
```

### LLM-Specific Optimizations

Add optimizations for new LLMs:

```python
if self.target_llm == TargetLLM.CUSTOM_LLM:
    constraints.extend([
        "Custom constraint for this LLM",
        "Another specific optimization",
    ])
```

---

## Best Practices

### Writing Effective Input

**Good Examples:**
- ✅ "Create a professional blog post about machine learning for beginners"
- ✅ "Write Python code to analyze CSV data and generate visualizations"
- ✅ "Explain blockchain technology to business executives using simple analogies"

**Less Effective:**
- ❌ "Write something" (too vague)
- ❌ "Help me" (no clear task)
- ❌ "Do the thing" (no context)

### Tips for Better Results

1. **Be Specific**: Include topic, audience, and desired outcome
2. **Mention Tone**: Specify if you want professional, casual, academic, etc.
3. **State Audience**: Mention who the content is for (beginners, experts, etc.)
4. **Include Format**: Specify if you want code, markdown, lists, etc.
5. **Add Constraints**: Mention length, complexity, or style requirements

### Choosing the Right LLM Target

- **Claude 3.5 Sonnet**: Best for detailed reasoning, long-form content, complex tasks
- **Claude 3.5 Haiku**: Best for quick responses, concise content, simple tasks
- **GPT-4 Turbo**: Best for creative tasks, balanced outputs, general purpose
- **GPT-4o**: Latest GPT-4 variant with improved capabilities
- **Gemini Pro**: Best for multimodal tasks, comprehensive context handling

---

## Examples

### Example 1: Content Creation

**Input:**
```
Write a blog post about sustainable living for millennials
```

**Generated Prompt Includes:**
- Role: Expert content creator specializing in sustainability
- Instructions: Create engaging headline, 5 sections, actionable tips
- Constraints: 1500 words, accessible language, SEO-optimized
- Quality Criteria: Engagement, value, clarity, actionability

### Example 2: Agent Development

**Input:**
```
Create a customer service chatbot that handles complaints professionally and empathetically
```

**Generated Prompt Includes:**
- Role: AI agent developer specializing in conversational AI
- Instructions: Define personality, conversation flows, error handling
- Constraints: Consistent tone, empathetic responses, solution-focused
- Quality Criteria: Helpfulness, professionalism, problem resolution

### Example 3: Educational Content

**Input:**
```
Explain quantum computing to high school students using simple analogies
```

**Generated Prompt Includes:**
- Role: Experienced educator with physics expertise
- Instructions: Use relatable analogies, build from basics, include examples
- Constraints: No jargon, age-appropriate, engaging
- Quality Criteria: Clarity, accuracy, pedagogical value

### Example 4: Technical Task

**Input:**
```
Write Python code to read CSV files, validate data, and generate summary statistics
```

**Generated Prompt Includes:**
- Role: Senior software engineer with data processing expertise
- Instructions: Clean code, error handling, documentation, examples
- Constraints: PEP 8 standards, production-ready, maintainable
- Quality Criteria: Correctness, readability, efficiency, best practices

### Example 5: Business Strategy

**Input:**
```
Develop a market entry strategy for a sustainable fashion brand targeting millennials
```

**Generated Prompt Includes:**
- Role: Business strategist with fashion industry expertise
- Instructions: SWOT analysis, objectives, tactics, implementation roadmap
- Constraints: Realistic, market-aware, aligned with goals
- Quality Criteria: Feasibility, alignment, clarity, impact

### Example 6: Data Analysis

**Input:**
```
Analyze customer purchase data to identify trends and provide actionable recommendations
```

**Generated Prompt Includes:**
- Role: Data analyst specializing in customer behavior
- Instructions: Exploratory analysis, pattern identification, visualizations
- Constraints: Evidence-based, acknowledge limitations, clear presentation
- Quality Criteria: Rigor, accuracy, clarity, actionability

---

## Troubleshooting

### Common Issues

**Issue**: Generated prompt is too generic
- **Solution**: Provide more specific input with details about audience, tone, and requirements

**Issue**: Wrong category detected
- **Solution**: Use more explicit keywords (e.g., "analyze data" instead of "look at data")

**Issue**: Missing important constraints
- **Solution**: Mention specific requirements in your input (e.g., "keep it under 500 words")

### Getting Help

- Check the demo: `python demo.py`
- Run tests: `python test_architect.py`
- Review examples in this guide
- Experiment with different inputs in the Streamlit interface

---

## Next Steps

1. **Experiment**: Try different inputs and see how the system adapts
2. **Customize**: Modify templates or detection logic for your specific needs
3. **Integrate**: Use the Python API in your own applications
4. **Share**: Generate prompts for your team or community

---

**Happy Prompt Engineering! 🏗️**

For more information, see [README.md](README.md)
