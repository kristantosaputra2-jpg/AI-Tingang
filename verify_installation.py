"""
Installation Verification Script
Checks that all components are properly installed and working
"""

import sys
import importlib


def check_imports():
    """Check that all required modules can be imported"""
    print("=" * 80)
    print("CHECKING IMPORTS")
    print("=" * 80)
    
    required_modules = [
        ("streamlit", "Streamlit UI framework"),
        ("prompt_architect", "Core prompt transformation engine"),
        ("prompt_templates", "Template library"),
    ]
    
    all_ok = True
    
    for module_name, description in required_modules:
        try:
            importlib.import_module(module_name)
            print(f"✓ {module_name:20s} - {description}")
        except ImportError as e:
            print(f"✗ {module_name:20s} - FAILED: {e}")
            all_ok = False
    
    return all_ok


def check_core_functionality():
    """Check that core functionality works"""
    print("\n" + "=" * 80)
    print("CHECKING CORE FUNCTIONALITY")
    print("=" * 80)
    
    try:
        from prompt_architect import create_architect
        
        print("\n1. Creating architect instance...")
        architect = create_architect("claude-3.5-sonnet")
        print("   ✓ Architect created successfully")
        
        print("\n2. Testing context extraction...")
        context = architect.extract_context("Write a blog post about AI")
        print(f"   ✓ Context extracted: intent={context.intent}, category={context.category.value}")
        
        print("\n3. Testing prompt transformation...")
        result = architect.transform("Create a simple tutorial")
        print(f"   ✓ Prompt generated: {len(result.full_prompt)} characters")
        
        print("\n4. Validating output structure...")
        assert result.role_definition, "Role definition missing"
        assert len(result.instructions) > 0, "Instructions missing"
        assert len(result.constraints) > 0, "Constraints missing"
        assert len(result.quality_criteria) > 0, "Quality criteria missing"
        print("   ✓ All components present")
        
        return True
        
    except Exception as e:
        print(f"   ✗ FAILED: {e}")
        return False


def check_template_library():
    """Check that template library works"""
    print("\n" + "=" * 80)
    print("CHECKING TEMPLATE LIBRARY")
    print("=" * 80)
    
    try:
        from prompt_templates import template_library
        
        print("\n1. Listing templates...")
        templates = template_library.list_templates()
        print(f"   ✓ Found {len(templates)} templates")
        
        print("\n2. Getting specific template...")
        template = template_library.get_template("blog_post")
        print(f"   ✓ Retrieved template: {template.name}")
        
        print("\n3. Filling template...")
        filled = template_library.fill_template("blog_post", template.example_values)
        print(f"   ✓ Template filled: {len(filled)} characters")
        
        print("\n4. Getting categories...")
        categories = template_library.get_categories()
        print(f"   ✓ Found {len(categories)} categories")
        
        return True
        
    except Exception as e:
        print(f"   ✗ FAILED: {e}")
        return False


def check_llm_support():
    """Check that all LLM targets are supported"""
    print("\n" + "=" * 80)
    print("CHECKING LLM SUPPORT")
    print("=" * 80)
    
    try:
        from prompt_architect import create_architect
        
        llm_models = [
            "claude-3.5-sonnet",
            "claude-3.5-haiku",
            "gpt-4-turbo",
            "gpt-4o",
            "gemini-pro"
        ]
        
        for llm in llm_models:
            architect = create_architect(llm)
            result = architect.transform("Test prompt")
            print(f"   ✓ {llm:20s} - {len(result.full_prompt)} chars")
        
        return True
        
    except Exception as e:
        print(f"   ✗ FAILED: {e}")
        return False


def check_files():
    """Check that all required files exist"""
    print("\n" + "=" * 80)
    print("CHECKING FILES")
    print("=" * 80)
    
    import os
    
    required_files = [
        ("app.py", "Streamlit application"),
        ("prompt_architect.py", "Core engine"),
        ("prompt_templates.py", "Template library"),
        ("requirements.txt", "Dependencies"),
        ("README.md", "Documentation"),
        ("USAGE_GUIDE.md", "Usage guide"),
        ("demo.py", "Demo script"),
        ("test_architect.py", "Test suite"),
    ]
    
    all_ok = True
    
    for filename, description in required_files:
        if os.path.exists(filename):
            size = os.path.getsize(filename)
            print(f"   ✓ {filename:25s} - {description} ({size:,} bytes)")
        else:
            print(f"   ✗ {filename:25s} - MISSING")
            all_ok = False
    
    return all_ok


def main():
    """Run all verification checks"""
    print("\n" + "🔍 " * 20)
    print("PROMPT ARCHITECT AGENT - INSTALLATION VERIFICATION")
    print("🔍 " * 20 + "\n")
    
    checks = [
        ("Imports", check_imports),
        ("Core Functionality", check_core_functionality),
        ("Template Library", check_template_library),
        ("LLM Support", check_llm_support),
        ("Files", check_files),
    ]
    
    results = {}
    
    for check_name, check_func in checks:
        try:
            results[check_name] = check_func()
        except Exception as e:
            print(f"\n✗ {check_name} check failed with exception: {e}")
            results[check_name] = False
    
    # Summary
    print("\n" + "=" * 80)
    print("VERIFICATION SUMMARY")
    print("=" * 80)
    
    for check_name, passed in results.items():
        status = "✅ PASSED" if passed else "❌ FAILED"
        print(f"{status:12s} - {check_name}")
    
    all_passed = all(results.values())
    
    print("\n" + "=" * 80)
    
    if all_passed:
        print("🎉 ALL CHECKS PASSED!")
        print("=" * 80)
        print("\nYour Prompt Architect Agent installation is ready to use!")
        print("\nNext steps:")
        print("  1. Run demo: python demo.py")
        print("  2. Run tests: python test_architect.py")
        print("  3. Start app: streamlit run app.py")
        print("\nFor more information, see USAGE_GUIDE.md")
        return 0
    else:
        print("❌ SOME CHECKS FAILED")
        print("=" * 80)
        print("\nPlease review the errors above and fix any issues.")
        print("If you need help, check README.md or USAGE_GUIDE.md")
        return 1


if __name__ == "__main__":
    sys.exit(main())
