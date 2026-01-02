# 🏗️ Prompt Architect Agent

**Transform raw ideas into highly detailed, structured prompts for any LLM**

Prompt Architect Agent is an advanced AI system that automatically converts brief user ideas into comprehensive, optimized prompts for Large Language Models. No prompt engineering knowledge required!

## ✨ Features

### 🎯 Automatic Context Extraction
- **Intent Detection**: Automatically identifies what you want to accomplish (create, analyze, explain, etc.)
- **Category Classification**: Determines the type of task (content creation, agent development, educational, etc.)
- **Audience Detection**: Identifies target audience (beginners, experts, professionals, etc.)
- **Tone Analysis**: Detects desired communication style (professional, casual, academic, etc.)
- **Output Format Recognition**: Determines preferred format (markdown, JSON, code, etc.)

### 🎭 Intelligent Role Definition
- Generates appropriate AI persona based on task requirements
- Adds specialization based on detected keywords
- Includes tone modifiers for communication style
- Optimized for target LLM capabilities

### 📋 Structured Instructions
- Layered, hierarchical instruction generation
- Audience-appropriate explanations
- Complexity-based guidance
- Format-specific directives
- Keyword-focused coverage

### ⚠️ Comprehensive Constraints
- LLM-specific optimization (Claude 3.5 Sonnet, GPT-4, etc.)
- Quality assurance guidelines
- Tone and style enforcement
- Length and format constraints
- Accuracy and factuality requirements

### ✅ Quality Evaluation Criteria
- Relevance, accuracy, clarity, completeness metrics
- Category-specific evaluation standards
- Tone-appropriate quality measures
- Actionable assessment criteria

### 📚 Template Library
Pre-built templates for common use cases:
- **Content Creation**: Blog posts, articles, marketing copy
- **Agent Development**: Chatbots, assistants, specialized agents
- **Educational**: Tutorials, courses, learning materials
- **Business**: Strategies, proposals, plans
- **Technical**: Code generation, documentation, debugging
- **Creative**: Stories, narratives, creative writing
- **Analysis**: Data analysis, research, reports

## 🚀 Quick Start

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd prompt-architect-agent
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

### Running the Application

Start the Streamlit interface:
```bash
streamlit run app.py
```

The application will open in your browser at `http://localhost:8501`

## 💡 Usage

### Basic Usage

1. **Enter Your Idea**: Simply type what you want in plain language
   ```
   Example: "Create a chatbot that helps students learn math"
   ```

2. **Select Target LLM**: Choose which LLM you're optimizing for
   - Claude 3.5 Sonnet (default, recommended)
   - Claude 3.5 Haiku
   - GPT-4 Turbo
   - GPT-4o
   - Gemini Pro

3. **Generate**: Click "Generate Structured Prompt"

4. **Review & Use**: Copy the generated prompt and use it with your chosen LLM

### Advanced Usage

#### Using the Python API

```python
from prompt_architect import create_architect

# Create architect instance
architect = create_architect(target_llm="claude-3.5-sonnet")

# Transform raw input
raw_input = "Write a blog post about AI ethics for beginners"
result = architect.transform(raw_input)

# Access components
print(result.role_definition)
print(result.instructions)
print(result.full_prompt)
```

#### Using Templates

```python
from prompt_templates import template_library

# List available templates
templates = template_library.list_templates()

# Get a specific template
template = template_library.get_template("blog_post")

# Fill template with values
values = {
    "topic": "artificial intelligence",
    "audience": "beginners",
    "num_sections": "5",
    "tone": "friendly",
    "word_count": "1500"
}
filled_prompt = template_library.fill_template("blog_post", values)
```

## 📖 Examples

### Example 1: Content Creation
**Input**: "Write a blog post about sustainable living for millennials"

**Generated Prompt Includes**:
- Role: Expert content writer specializing in sustainability
- Instructions: Create engaging headline, 5 main sections, actionable tips
- Constraints: 1500 words, accessible language, SEO-optimized
- Quality Criteria: Engagement, value, clarity, actionability

### Example 2: Agent Development
**Input**: "Create a customer service bot that handles complaints professionally"

**Generated Prompt Includes**:
- Role: AI agent developer specializing in conversational AI
- Instructions: Define personality, conversation flows, error handling
- Constraints: Consistent tone, empathetic responses, solution-focused
- Quality Criteria: Helpfulness, professionalism, problem resolution

### Example 3: Educational Content
**Input**: "Explain quantum computing to high school students using simple analogies"

**Generated Prompt Includes**:
- Role: Experienced educator with physics expertise
- Instructions: Use relatable analogies, build from basics, include examples
- Constraints: No jargon, age-appropriate, engaging
- Quality Criteria: Clarity, accuracy, pedagogical value

## 🎨 Customization

### Adding Custom Templates

Edit `prompt_templates.py` to add your own templates:

```python
templates["custom_template"] = PromptTemplate(
    name="Your Template Name",
    category="Your Category",
    description="Template description",
    template="Your template with {variables}",
    variables=["variable1", "variable2"],
    example_values={"variable1": "example1", "variable2": "example2"}
)
```

### Modifying Detection Logic

Edit `prompt_architect.py` to customize:
- Intent detection keywords
- Category classification
- Tone indicators
- Output format detection

## 🏗️ Architecture

### Core Components

1. **PromptArchitect** (`prompt_architect.py`)
   - Main transformation engine
   - Context extraction
   - Component generation
   - Prompt assembly

2. **TemplateLibrary** (`prompt_templates.py`)
   - Pre-built templates
   - Template management
   - Variable substitution

3. **Streamlit Interface** (`app.py`)
   - User interface
   - Configuration options
   - Result display
   - Export functionality

### Data Flow

```
Raw Input → Context Extraction → Component Generation → Prompt Assembly → Structured Output
```

## 🎯 Optimization for Different LLMs

### Claude 3.5 Sonnet (Recommended)
- Optimized for long-form reasoning
- Detailed instructions and context
- Structured hierarchical prompts
- Emphasis on accuracy and consistency

### GPT-4 Turbo / GPT-4o
- Balanced creativity and accuracy
- Flexible instruction following
- Natural conversation flow

### Gemini Pro
- Multi-modal capabilities
- Comprehensive context handling
- Structured output generation

## 📊 Quality Assurance

The system ensures high-quality prompts through:
- **Automatic validation** of generated components
- **Consistency checks** across all sections
- **LLM-specific optimization** for target model
- **Quality criteria** for output evaluation

## 🛠️ Technical Details

### Requirements
- Python 3.8+
- Streamlit 1.52.0+
- No external API dependencies for core functionality

### Project Structure
```
prompt-architect-agent/
├── app.py                  # Streamlit interface
├── prompt_architect.py     # Core transformation engine
├── prompt_templates.py     # Template library
├── requirements.txt        # Python dependencies
└── README.md              # Documentation
```

## 🤝 Contributing

Contributions are welcome! Areas for improvement:
- Additional templates for specific use cases
- Enhanced detection algorithms
- Support for more LLMs
- Multi-language support
- Advanced customization options

## 📝 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

Optimized for Claude 3.5 Sonnet with compatibility for GPT-4 and other leading LLMs.

## 📧 Support

For issues, questions, or suggestions, please open an issue on the repository.

---

**Made with ❤️ for the AI community**

Transform any idea into a production-ready prompt in seconds!
