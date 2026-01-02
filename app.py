"""
Prompt Architect Agent - Streamlit Interface
Transform raw ideas into highly detailed, structured prompts for any LLM
"""

import streamlit as st
from prompt_architect import create_architect, TargetLLM, PromptCategory
import json

# -----------------------------------------------------
# 1. PAGE CONFIGURATION
# -----------------------------------------------------
st.set_page_config(
    page_title="Prompt Architect Agent",
    page_icon="🏗️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------------------------------
# 2. CUSTOM CSS
# -----------------------------------------------------
st.markdown("""
    <style>
    /* Modern gradient background */
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    /* Card-like containers */
    .main .block-container {
        padding: 2rem;
        background: rgba(255, 255, 255, 0.95);
        border-radius: 15px;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
    }
    
    /* Headers */
    h1 {
        color: #667eea;
        font-weight: 700;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    
    h2 {
        color: #764ba2;
        font-weight: 600;
        border-bottom: 2px solid #667eea;
        padding-bottom: 0.5rem;
    }
    
    h3 {
        color: #667eea;
        font-weight: 600;
    }
    
    /* Text areas */
    .stTextArea textarea {
        border: 2px solid #667eea;
        border-radius: 10px;
        font-size: 16px;
    }
    
    /* Buttons */
    .stButton button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        font-weight: 600;
        border: none;
        border-radius: 10px;
        padding: 0.75rem 2rem;
        font-size: 18px;
        transition: transform 0.2s;
    }
    
    .stButton button:hover {
        transform: scale(1.05);
        box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
    }
    
    /* Info boxes */
    .stAlert {
        border-radius: 10px;
        border-left: 5px solid #667eea;
    }
    
    /* Sidebar */
    .css-1d391kg {
        background: linear-gradient(180deg, #667eea 0%, #764ba2 100%);
    }
    
    /* Code blocks */
    .stCodeBlock {
        border-radius: 10px;
        border: 2px solid #667eea;
    }
    
    /* Expander */
    .streamlit-expanderHeader {
        background-color: #f0f2f6;
        border-radius: 10px;
        font-weight: 600;
    }
    </style>
""", unsafe_allow_html=True)

# -----------------------------------------------------
# 3. SIDEBAR CONFIGURATION
# -----------------------------------------------------
with st.sidebar:
    st.title("🏗️ Prompt Architect")
    st.markdown("---")
    
    st.subheader("⚙️ Configuration")
    
    # Target LLM Selection
    target_llm = st.selectbox(
        "Target LLM",
        options=[
            "claude-3.5-sonnet",
            "claude-3.5-haiku",
            "gpt-4-turbo",
            "gpt-4o",
            "gemini-pro"
        ],
        index=0,
        help="Select the LLM you want to optimize the prompt for"
    )
    
    st.markdown("---")
    
    # Advanced Options
    with st.expander("🔧 Advanced Options"):
        show_context = st.checkbox("Show Extracted Context", value=True)
        show_components = st.checkbox("Show Prompt Components", value=True)
        enable_copy = st.checkbox("Enable Copy Buttons", value=True)
    
    st.markdown("---")
    
    # Information
    st.subheader("ℹ️ About")
    st.info("""
    **Prompt Architect Agent** transforms your raw ideas into highly detailed, 
    structured prompts optimized for any LLM.
    
    **Features:**
    - 🎯 Automatic intent detection
    - 🎭 Role definition generation
    - 📋 Structured instructions
    - ✅ Quality criteria
    - 🎨 Tone & style optimization
    """)
    
    st.markdown("---")
    
    # Examples
    st.subheader("💡 Quick Examples")
    example_prompts = {
        "Content Creation": "Write a blog post about AI ethics for beginners",
        "Agent Development": "Create a customer service chatbot that handles complaints professionally",
        "Educational": "Explain quantum computing to high school students using simple analogies",
        "Business": "Develop a marketing strategy for a new eco-friendly product",
        "Technical": "Write Python code to analyze CSV data and create visualizations",
    }
    
    selected_example = st.selectbox(
        "Load Example",
        options=[""] + list(example_prompts.keys())
    )
    
    if selected_example and st.button("Load Example"):
        st.session_state.example_loaded = example_prompts[selected_example]

# -----------------------------------------------------
# 4. MAIN INTERFACE
# -----------------------------------------------------

# Header
st.title("🏗️ Prompt Architect Agent")
st.markdown("""
<p style='text-align: center; font-size: 18px; color: #666;'>
Transform raw ideas into highly detailed, structured prompts for any LLM
</p>
""", unsafe_allow_html=True)

st.markdown("---")

# Initialize architect
if 'architect' not in st.session_state or st.session_state.get('current_llm') != target_llm:
    st.session_state.architect = create_architect(target_llm)
    st.session_state.current_llm = target_llm

architect = st.session_state.architect

# Input Section
st.subheader("📝 Your Idea")
st.markdown("Enter your raw idea below. No prompt engineering knowledge required!")

# Load example if available
default_value = st.session_state.get('example_loaded', '')
if default_value:
    st.session_state.pop('example_loaded', None)

user_input = st.text_area(
    "Raw Input",
    value=default_value,
    height=150,
    placeholder="Example: Create a chatbot that helps students learn math by explaining concepts step by step...",
    help="Describe what you want in plain language. The system will extract intent, tone, audience, and more automatically.",
    label_visibility="collapsed"
)

# Generate Button
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    generate_button = st.button("🚀 Generate Structured Prompt", use_container_width=True)

# -----------------------------------------------------
# 5. PROMPT GENERATION & DISPLAY
# -----------------------------------------------------

if generate_button and user_input.strip():
    with st.spinner("🔄 Analyzing your input and generating structured prompt..."):
        try:
            # Transform input
            result = architect.transform(user_input)
            
            st.success("✅ Prompt generated successfully!")
            
            st.markdown("---")
            
            # Display Extracted Context
            if show_context:
                st.subheader("🔍 Extracted Context")
                
                context = architect.extract_context(user_input)
                
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    st.metric("Intent", context.intent.replace("_", " ").title())
                    st.metric("Category", context.category.value.replace("_", " ").title())
                
                with col2:
                    st.metric("Audience", context.target_audience.replace("_", " ").title())
                    st.metric("Tone", context.tone.title())
                
                with col3:
                    st.metric("Output Format", context.output_format.replace("_", " ").title())
                    st.metric("Complexity", context.complexity_level.title())
                
                if context.keywords:
                    st.markdown("**Keywords:** " + ", ".join(f"`{kw}`" for kw in context.keywords))
                
                st.markdown("---")
            
            # Display Prompt Components
            if show_components:
                st.subheader("🧩 Prompt Components")
                
                # Role Definition
                with st.expander("🎭 Role Definition", expanded=True):
                    st.markdown(result.role_definition)
                    if enable_copy:
                        st.code(result.role_definition, language=None)
                
                # Instructions
                with st.expander("📋 Instructions", expanded=True):
                    for i, instruction in enumerate(result.instructions, 1):
                        st.markdown(f"{i}. {instruction}")
                    if enable_copy:
                        st.code("\n".join(f"{i}. {inst}" for i, inst in enumerate(result.instructions, 1)), language=None)
                
                # Constraints
                with st.expander("⚠️ Constraints", expanded=False):
                    for constraint in result.constraints:
                        st.markdown(f"- {constraint}")
                    if enable_copy:
                        st.code("\n".join(f"- {c}" for c in result.constraints), language=None)
                
                # Quality Criteria
                with st.expander("✅ Quality Criteria", expanded=False):
                    for criterion in result.quality_criteria:
                        st.markdown(f"- {criterion}")
                    if enable_copy:
                        st.code("\n".join(f"- {qc}" for qc in result.quality_criteria), language=None)
                
                st.markdown("---")
            
            # Full Structured Prompt
            st.subheader("📄 Complete Structured Prompt")
            st.markdown("Copy this prompt and use it with your chosen LLM:")
            
            # Display in a nice code block
            st.code(result.full_prompt, language="markdown")
            
            # Download button
            st.download_button(
                label="📥 Download Prompt",
                data=result.full_prompt,
                file_name="structured_prompt.md",
                mime="text/markdown",
                use_container_width=True
            )
            
            # JSON Export
            with st.expander("📊 Export as JSON"):
                json_data = {
                    "role_definition": result.role_definition,
                    "context": result.context,
                    "instructions": result.instructions,
                    "constraints": result.constraints,
                    "output_format": result.output_format,
                    "quality_criteria": result.quality_criteria,
                    "target_llm": target_llm
                }
                st.json(json_data)
                st.download_button(
                    label="📥 Download JSON",
                    data=json.dumps(json_data, indent=2),
                    file_name="structured_prompt.json",
                    mime="application/json"
                )
            
        except Exception as e:
            st.error(f"❌ Error generating prompt: {str(e)}")
            st.exception(e)

elif generate_button:
    st.warning("⚠️ Please enter your idea first!")

# -----------------------------------------------------
# 6. FOOTER
# -----------------------------------------------------

st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 2rem;'>
    <p><strong>Prompt Architect Agent</strong> - Optimized for Claude 3.5 Sonnet</p>
    <p>Transform any idea into a production-ready prompt in seconds</p>
</div>
""", unsafe_allow_html=True)
