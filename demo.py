"""
Quick Demo of Prompt Architect Agent
Shows basic usage and example outputs
"""

from prompt_architect import create_architect
from prompt_templates import template_library


def demo_basic_usage():
    """Demonstrate basic usage"""
    print("=" * 80)
    print("PROMPT ARCHITECT AGENT - BASIC DEMO")
    print("=" * 80)
    
    # Create architect
    architect = create_architect("claude-3.5-sonnet")
    
    # Example 1: Simple content creation
    print("\n📝 Example 1: Content Creation")
    print("-" * 80)
    
    raw_input = "Write a blog post about sustainable living for millennials"
    print(f"Input: {raw_input}\n")
    
    result = architect.transform(raw_input)
    
    print("Generated Prompt:")
    print(result.full_prompt)
    print("\n" + "=" * 80)
    
    # Example 2: Agent development
    print("\n🤖 Example 2: Agent Development")
    print("-" * 80)
    
    raw_input = "Create a customer service chatbot that handles complaints professionally"
    print(f"Input: {raw_input}\n")
    
    result = architect.transform(raw_input)
    
    print("Role Definition:")
    print(result.role_definition)
    print("\nInstructions:")
    for i, instruction in enumerate(result.instructions, 1):
        print(f"{i}. {instruction}")
    print("\n" + "=" * 80)
    
    # Example 3: Educational content
    print("\n📚 Example 3: Educational Content")
    print("-" * 80)
    
    raw_input = "Explain machine learning to high school students using simple analogies"
    print(f"Input: {raw_input}\n")
    
    result = architect.transform(raw_input)
    
    print("Quality Criteria:")
    for criterion in result.quality_criteria:
        print(f"- {criterion}")
    print("\n" + "=" * 80)


def demo_template_usage():
    """Demonstrate template library usage"""
    print("\n📚 TEMPLATE LIBRARY DEMO")
    print("=" * 80)
    
    # List available templates
    print("\nAvailable Templates:")
    for i, template_name in enumerate(template_library.list_templates(), 1):
        template = template_library.get_template(template_name)
        print(f"{i}. {template.name} ({template.category})")
    
    # Use a template
    print("\n" + "-" * 80)
    print("Using 'blog_post' template:")
    print("-" * 80)
    
    blog_template = template_library.get_template("blog_post")
    
    custom_values = {
        "topic": "artificial intelligence in healthcare",
        "audience": "healthcare professionals",
        "num_sections": "5",
        "tone": "professional yet accessible",
        "word_count": "1500"
    }
    
    filled_prompt = template_library.fill_template("blog_post", custom_values)
    print(filled_prompt)
    print("\n" + "=" * 80)


def demo_context_extraction():
    """Demonstrate context extraction"""
    print("\n🔍 CONTEXT EXTRACTION DEMO")
    print("=" * 80)
    
    architect = create_architect("claude-3.5-sonnet")
    
    test_inputs = [
        "Create a professional technical guide for experts",
        "Write a casual blog post for beginners",
        "Analyze customer data and provide insights",
    ]
    
    for i, raw_input in enumerate(test_inputs, 1):
        print(f"\n{i}. Input: {raw_input}")
        print("-" * 80)
        
        context = architect.extract_context(raw_input)
        
        print(f"Intent: {context.intent}")
        print(f"Category: {context.category.value}")
        print(f"Audience: {context.target_audience}")
        print(f"Tone: {context.tone}")
        print(f"Output Format: {context.output_format}")
        print(f"Complexity: {context.complexity_level}")
        print(f"Keywords: {', '.join(context.keywords[:5])}")
    
    print("\n" + "=" * 80)


def demo_llm_optimization():
    """Demonstrate LLM-specific optimization"""
    print("\n⚙️ LLM OPTIMIZATION DEMO")
    print("=" * 80)
    
    raw_input = "Write a technical article about neural networks"
    
    llm_models = ["claude-3.5-sonnet", "gpt-4-turbo", "gemini-pro"]
    
    for llm in llm_models:
        print(f"\n🎯 Optimized for: {llm}")
        print("-" * 80)
        
        architect = create_architect(llm)
        result = architect.transform(raw_input)
        
        print("Constraints:")
        for constraint in result.constraints[:3]:
            print(f"- {constraint}")
        print(f"... and {len(result.constraints) - 3} more")
    
    print("\n" + "=" * 80)


def main():
    """Run all demos"""
    print("\n" + "🏗️ " * 20)
    print("PROMPT ARCHITECT AGENT - COMPREHENSIVE DEMO")
    print("🏗️ " * 20)
    
    demo_basic_usage()
    demo_template_usage()
    demo_context_extraction()
    demo_llm_optimization()
    
    print("\n" + "=" * 80)
    print("✅ DEMO COMPLETE!")
    print("=" * 80)
    print("\nTo use the interactive Streamlit interface, run:")
    print("  streamlit run app.py")
    print("\nFor more information, see README.md")
    print("=" * 80 + "\n")


if __name__ == "__main__":
    main()
