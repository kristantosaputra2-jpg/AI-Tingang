"""
Test suite for Prompt Architect Agent
Tests various input scenarios and validates output quality
"""

from prompt_architect import create_architect, PromptCategory
from prompt_templates import template_library


def test_basic_transformation():
    """Test basic prompt transformation"""
    print("=" * 80)
    print("TEST 1: Basic Transformation")
    print("=" * 80)
    
    architect = create_architect("claude-3.5-sonnet")
    
    test_inputs = [
        "Write a blog post about AI ethics for beginners",
        "Create a chatbot that helps students learn math",
        "Explain quantum computing to high school students",
        "Develop a marketing strategy for a new product",
        "Write Python code to analyze CSV data",
    ]
    
    for i, raw_input in enumerate(test_inputs, 1):
        print(f"\n--- Test Case {i} ---")
        print(f"Input: {raw_input}")
        
        result = architect.transform(raw_input)
        
        print(f"✓ Role: {result.role_definition[:80]}...")
        print(f"✓ Instructions: {len(result.instructions)} items")
        print(f"✓ Constraints: {len(result.constraints)} items")
        print(f"✓ Quality Criteria: {len(result.quality_criteria)} items")
        print(f"✓ Full Prompt Length: {len(result.full_prompt)} characters")
        
        # Validate structure
        assert result.role_definition, "Role definition should not be empty"
        assert len(result.instructions) > 0, "Should have instructions"
        assert len(result.constraints) > 0, "Should have constraints"
        assert len(result.quality_criteria) > 0, "Should have quality criteria"
        assert len(result.full_prompt) > 100, "Full prompt should be substantial"
        
    print("\n✅ All basic transformation tests passed!")


def test_context_extraction():
    """Test context extraction accuracy"""
    print("\n" + "=" * 80)
    print("TEST 2: Context Extraction")
    print("=" * 80)
    
    architect = create_architect("claude-3.5-sonnet")
    
    test_cases = [
        {
            "input": "Create a professional blog post about machine learning for experts",
            "expected": {
                "intent": "create",
                "tone": "professional",
                "audience": "experts",
            }
        },
        {
            "input": "Analyze sales data and provide detailed insights",
            "expected": {
                "intent": "analyze",
                "category": PromptCategory.ANALYSIS,
            }
        },
        {
            "input": "Write a casual tutorial teaching beginners about history",
            "expected": {
                "intent": "create",
                "tone": "casual",
                "audience": "beginners",
                "category": PromptCategory.EDUCATIONAL,
            }
        },
    ]
    
    for i, test_case in enumerate(test_cases, 1):
        print(f"\n--- Test Case {i} ---")
        print(f"Input: {test_case['input']}")
        
        context = architect.extract_context(test_case['input'])
        
        print(f"Extracted Context:")
        print(f"  Intent: {context.intent}")
        print(f"  Category: {context.category.value}")
        print(f"  Audience: {context.target_audience}")
        print(f"  Tone: {context.tone}")
        print(f"  Output Format: {context.output_format}")
        print(f"  Complexity: {context.complexity_level}")
        print(f"  Keywords: {', '.join(context.keywords[:5])}")
        
        # Validate expected values
        expected = test_case['expected']
        if 'intent' in expected:
            assert context.intent == expected['intent'], f"Expected intent '{expected['intent']}', got '{context.intent}'"
        if 'tone' in expected:
            assert context.tone == expected['tone'], f"Expected tone '{expected['tone']}', got '{context.tone}'"
        if 'audience' in expected:
            assert context.target_audience == expected['audience'], f"Expected audience '{expected['audience']}', got '{context.target_audience}'"
        if 'category' in expected:
            assert context.category == expected['category'], f"Expected category '{expected['category']}', got '{context.category}'"
        
        print("✓ Context extraction validated")
    
    print("\n✅ All context extraction tests passed!")


def test_llm_optimization():
    """Test LLM-specific optimization"""
    print("\n" + "=" * 80)
    print("TEST 3: LLM-Specific Optimization")
    print("=" * 80)
    
    test_input = "Write a technical article about neural networks"
    
    llm_models = [
        "claude-3.5-sonnet",
        "gpt-4-turbo",
        "gemini-pro"
    ]
    
    for llm in llm_models:
        print(f"\n--- Testing {llm} ---")
        
        architect = create_architect(llm)
        result = architect.transform(test_input)
        
        print(f"✓ Generated prompt for {llm}")
        print(f"  Constraints: {len(result.constraints)}")
        
        # Check for LLM-specific constraints
        constraint_text = " ".join(result.constraints).lower()
        
        if "claude" in llm:
            assert "reasoning" in constraint_text or "detailed" in constraint_text, \
                "Claude prompts should emphasize reasoning"
            print("  ✓ Contains Claude-specific optimizations")
        
        print(f"  Full prompt length: {len(result.full_prompt)} characters")
    
    print("\n✅ All LLM optimization tests passed!")


def test_template_library():
    """Test template library functionality"""
    print("\n" + "=" * 80)
    print("TEST 4: Template Library")
    print("=" * 80)
    
    # Test listing templates
    templates = template_library.list_templates()
    print(f"\n✓ Found {len(templates)} templates")
    print(f"  Templates: {', '.join(templates)}")
    
    assert len(templates) > 0, "Should have templates"
    
    # Test getting categories
    categories = template_library.get_categories()
    print(f"\n✓ Found {len(categories)} categories")
    print(f"  Categories: {', '.join(categories)}")
    
    # Test getting specific template
    blog_template = template_library.get_template("blog_post")
    assert blog_template is not None, "Should find blog_post template"
    print(f"\n✓ Retrieved 'blog_post' template")
    print(f"  Name: {blog_template.name}")
    print(f"  Category: {blog_template.category}")
    print(f"  Variables: {', '.join(blog_template.variables)}")
    
    # Test filling template
    filled = template_library.fill_template("blog_post", blog_template.example_values)
    assert len(filled) > 0, "Filled template should not be empty"
    assert "{topic}" not in filled, "All variables should be replaced"
    print(f"\n✓ Successfully filled template")
    print(f"  Length: {len(filled)} characters")
    
    # Test getting templates by category
    content_templates = template_library.get_templates_by_category("Content Creation")
    print(f"\n✓ Found {len(content_templates)} Content Creation templates")
    
    print("\n✅ All template library tests passed!")


def test_edge_cases():
    """Test edge cases and error handling"""
    print("\n" + "=" * 80)
    print("TEST 5: Edge Cases")
    print("=" * 80)
    
    architect = create_architect("claude-3.5-sonnet")
    
    edge_cases = [
        "help",  # Very short input
        "I need something but I'm not sure what",  # Vague input
        "Create a super detailed comprehensive exhaustive complete thorough blog post",  # Redundant
        "Write code in Python to do machine learning with data analysis and visualization",  # Multiple topics
    ]
    
    for i, test_input in enumerate(edge_cases, 1):
        print(f"\n--- Edge Case {i} ---")
        print(f"Input: {test_input}")
        
        try:
            result = architect.transform(test_input)
            print(f"✓ Successfully handled edge case")
            print(f"  Generated {len(result.instructions)} instructions")
            print(f"  Prompt length: {len(result.full_prompt)} characters")
            
            assert result.full_prompt, "Should generate valid prompt even for edge cases"
            
        except Exception as e:
            print(f"✗ Failed with error: {e}")
            raise
    
    print("\n✅ All edge case tests passed!")


def test_output_quality():
    """Test output quality and completeness"""
    print("\n" + "=" * 80)
    print("TEST 6: Output Quality")
    print("=" * 80)
    
    architect = create_architect("claude-3.5-sonnet")
    
    test_input = "Create an educational tutorial about Python programming for beginners"
    result = architect.transform(test_input)
    
    print(f"\nAnalyzing output quality for: {test_input}")
    
    # Check completeness
    checks = {
        "Has role definition": bool(result.role_definition),
        "Has instructions": len(result.instructions) >= 3,
        "Has constraints": len(result.constraints) >= 3,
        "Has quality criteria": len(result.quality_criteria) >= 3,
        "Has full prompt": len(result.full_prompt) > 500,
        "Role mentions education": "educat" in result.role_definition.lower(),
        "Instructions mention beginners": any("beginner" in inst.lower() for inst in result.instructions),
        "Prompt is well-structured": "# Role Definition" in result.full_prompt,
    }
    
    print("\nQuality Checks:")
    for check, passed in checks.items():
        status = "✓" if passed else "✗"
        print(f"  {status} {check}")
        assert passed, f"Quality check failed: {check}"
    
    print("\n✅ All output quality tests passed!")


def run_all_tests():
    """Run all test suites"""
    print("\n" + "=" * 80)
    print("PROMPT ARCHITECT AGENT - TEST SUITE")
    print("=" * 80)
    
    try:
        test_basic_transformation()
        test_context_extraction()
        test_llm_optimization()
        test_template_library()
        test_edge_cases()
        test_output_quality()
        
        print("\n" + "=" * 80)
        print("🎉 ALL TESTS PASSED SUCCESSFULLY!")
        print("=" * 80)
        print("\nThe Prompt Architect Agent is working correctly.")
        print("You can now use it with confidence!")
        
    except AssertionError as e:
        print(f"\n❌ TEST FAILED: {e}")
        raise
    except Exception as e:
        print(f"\n❌ UNEXPECTED ERROR: {e}")
        raise


if __name__ == "__main__":
    run_all_tests()
