"""
Prompt Templates Library
Pre-built templates for common use cases
"""

from typing import Dict, List
from dataclasses import dataclass


@dataclass
class PromptTemplate:
    """Template structure for common prompt patterns"""
    name: str
    category: str
    description: str
    template: str
    variables: List[str]
    example_values: Dict[str, str]


class TemplateLibrary:
    """Library of pre-built prompt templates"""
    
    def __init__(self):
        self.templates = self._load_templates()
    
    def _load_templates(self) -> Dict[str, PromptTemplate]:
        """Load all available templates"""
        templates = {}
        
        # Content Creation Templates
        templates["blog_post"] = PromptTemplate(
            name="Blog Post Writer",
            category="Content Creation",
            description="Generate engaging blog posts on any topic",
            template="""# Role Definition
You are an expert content writer and blogger with years of experience creating engaging, SEO-optimized content.

# Task
Write a comprehensive blog post about {topic} for {audience}.

# Instructions
1. Create an attention-grabbing headline
2. Write an engaging introduction that hooks the reader
3. Develop {num_sections} main sections with clear subheadings
4. Include relevant examples and data to support your points
5. End with a compelling conclusion and call-to-action
6. Maintain a {tone} tone throughout

# Constraints
- Target length: {word_count} words
- Use simple, accessible language
- Include actionable takeaways
- Optimize for readability (short paragraphs, bullet points where appropriate)

# Output Format
Markdown with proper headers, emphasis, and formatting

# Quality Criteria
- Engagement: Content captures and maintains reader interest
- Value: Provides actionable insights and useful information
- Clarity: Easy to read and understand
- SEO: Naturally incorporates relevant keywords
""",
            variables=["topic", "audience", "num_sections", "tone", "word_count"],
            example_values={
                "topic": "artificial intelligence in healthcare",
                "audience": "healthcare professionals",
                "num_sections": "5",
                "tone": "professional yet accessible",
                "word_count": "1500"
            }
        )
        
        # Agent Development Templates
        templates["chatbot_agent"] = PromptTemplate(
            name="Chatbot Agent Developer",
            category="Agent Development",
            description="Design conversational AI agents with specific personalities and capabilities",
            template="""# Role Definition
You are an advanced AI agent developer specializing in conversational AI systems with expertise in natural language processing and user experience design.

# Task
Design a chatbot agent for {use_case} that serves {target_users}.

# Agent Specifications
- **Purpose**: {purpose}
- **Personality**: {personality}
- **Key Capabilities**: {capabilities}
- **Tone**: {tone}

# Instructions
1. Define the agent's core personality and communication style
2. Outline conversation flow and dialogue patterns
3. Specify how the agent should handle common user intents
4. Define error handling and fallback responses
5. Include example conversations demonstrating the agent's capabilities
6. Specify integration points and technical requirements

# Constraints
- Maintain consistent personality throughout all interactions
- Ensure responses are helpful, accurate, and appropriate
- Handle edge cases and unexpected inputs gracefully
- Prioritize user experience and satisfaction

# Output Format
Structured document with:
- Agent profile
- Conversation flows
- Sample dialogues
- Technical specifications

# Quality Criteria
- Consistency: Agent maintains personality across all interactions
- Helpfulness: Effectively assists users in achieving their goals
- Natural language: Conversations feel natural and engaging
- Robustness: Handles various inputs and edge cases appropriately
""",
            variables=["use_case", "target_users", "purpose", "personality", "capabilities", "tone"],
            example_values={
                "use_case": "customer support",
                "target_users": "e-commerce customers",
                "purpose": "resolve customer issues and answer product questions",
                "personality": "friendly, patient, and solution-oriented",
                "capabilities": "order tracking, returns processing, product recommendations",
                "tone": "professional yet warm and approachable"
            }
        )
        
        # Educational Templates
        templates["tutorial_creator"] = PromptTemplate(
            name="Tutorial Creator",
            category="Educational",
            description="Create comprehensive tutorials and learning materials",
            template="""# Role Definition
You are an experienced educator and instructional designer with expertise in creating effective learning materials for {subject_area}.

# Task
Create a comprehensive tutorial on {topic} for {learner_level} learners.

# Learning Objectives
By the end of this tutorial, learners will be able to:
{learning_objectives}

# Instructions
1. Start with prerequisites and what learners need to know beforehand
2. Break down the topic into logical, sequential lessons
3. For each lesson:
   - Explain the concept clearly with examples
   - Provide hands-on exercises or practice problems
   - Include visual aids or diagrams where helpful
4. Build complexity gradually from basic to advanced
5. Include checkpoints to assess understanding
6. Provide additional resources for further learning

# Constraints
- Use clear, jargon-free language (explain technical terms when necessary)
- Include practical, real-world examples
- Make content engaging and interactive
- Ensure accessibility for diverse learning styles

# Output Format
Structured tutorial with:
- Introduction and prerequisites
- Numbered lessons with clear sections
- Examples and exercises
- Summary and next steps

# Quality Criteria
- Clarity: Concepts are explained in an easy-to-understand manner
- Progression: Content builds logically from simple to complex
- Engagement: Material keeps learners interested and motivated
- Effectiveness: Learners can apply what they've learned
""",
            variables=["subject_area", "topic", "learner_level", "learning_objectives"],
            example_values={
                "subject_area": "programming",
                "topic": "Python functions and modules",
                "learner_level": "beginner",
                "learning_objectives": "1. Define and call functions\n2. Use parameters and return values\n3. Import and use modules\n4. Create their own modules"
            }
        )
        
        # Business Templates
        templates["business_strategy"] = PromptTemplate(
            name="Business Strategy Developer",
            category="Business",
            description="Develop comprehensive business strategies and plans",
            template="""# Role Definition
You are a seasoned business strategist and consultant with extensive experience in {industry} and proven track record of developing successful business strategies.

# Task
Develop a comprehensive {strategy_type} strategy for {business_description}.

# Business Context
- **Industry**: {industry}
- **Target Market**: {target_market}
- **Current Situation**: {current_situation}
- **Goals**: {goals}
- **Timeline**: {timeline}

# Instructions
1. Conduct situation analysis (SWOT or similar framework)
2. Define clear, measurable objectives
3. Identify key strategies and tactics to achieve objectives
4. Outline implementation roadmap with milestones
5. Define success metrics and KPIs
6. Address potential risks and mitigation strategies
7. Provide resource requirements and budget considerations

# Constraints
- Strategies must be realistic and achievable
- Consider market conditions and competitive landscape
- Align with business goals and values
- Focus on actionable recommendations

# Output Format
Structured business strategy document with:
- Executive summary
- Situation analysis
- Strategic objectives
- Action plans
- Metrics and evaluation

# Quality Criteria
- Feasibility: Strategies are realistic and implementable
- Alignment: Plans align with business goals and resources
- Clarity: Recommendations are clear and actionable
- Impact: Strategies have potential for significant positive impact
""",
            variables=["industry", "strategy_type", "business_description", "target_market", 
                      "current_situation", "goals", "timeline"],
            example_values={
                "industry": "sustainable fashion",
                "strategy_type": "market entry",
                "business_description": "eco-friendly clothing brand targeting millennials",
                "target_market": "environmentally conscious consumers aged 25-40",
                "current_situation": "established online presence, planning retail expansion",
                "goals": "open 5 physical stores in major cities within 18 months",
                "timeline": "18 months"
            }
        )
        
        # Technical Templates
        templates["code_generator"] = PromptTemplate(
            name="Code Generator",
            category="Technical",
            description="Generate clean, well-documented code for specific tasks",
            template="""# Role Definition
You are a senior software engineer with expertise in {programming_language} and {domain}, known for writing clean, efficient, and well-documented code.

# Task
Write {code_type} in {programming_language} that {functionality}.

# Requirements
{requirements}

# Instructions
1. Write clean, readable code following {programming_language} best practices
2. Include comprehensive comments explaining complex logic
3. Implement proper error handling
4. Follow {coding_standard} coding standards
5. Include docstrings/documentation for functions and classes
6. Provide usage examples
7. Consider edge cases and input validation

# Constraints
- Code must be production-ready and maintainable
- Follow DRY (Don't Repeat Yourself) principle
- Optimize for readability over cleverness
- Include type hints/annotations where applicable
- No external dependencies unless specified

# Output Format
- Complete, runnable code
- Inline comments for complex sections
- Documentation/docstrings
- Usage examples

# Quality Criteria
- Correctness: Code works as intended and handles edge cases
- Readability: Code is easy to understand and maintain
- Efficiency: Code performs well and uses resources appropriately
- Best practices: Follows language conventions and design patterns
""",
            variables=["programming_language", "domain", "code_type", "functionality", 
                      "requirements", "coding_standard"],
            example_values={
                "programming_language": "Python",
                "domain": "data processing",
                "code_type": "a class",
                "functionality": "reads CSV files, performs data validation, and generates summary statistics",
                "requirements": "- Support multiple CSV formats\n- Validate data types\n- Handle missing values\n- Generate mean, median, mode statistics\n- Export results to JSON",
                "coding_standard": "PEP 8"
            }
        )
        
        # Analysis Templates
        templates["data_analyst"] = PromptTemplate(
            name="Data Analysis Expert",
            category="Analysis",
            description="Perform comprehensive data analysis and generate insights",
            template="""# Role Definition
You are a data analyst and research specialist with expertise in {analysis_domain} and strong skills in statistical analysis and data interpretation.

# Task
Analyze {data_description} and provide comprehensive insights about {analysis_focus}.

# Analysis Requirements
- **Data Source**: {data_source}
- **Key Questions**: {key_questions}
- **Analysis Type**: {analysis_type}
- **Deliverables**: {deliverables}

# Instructions
1. Describe the dataset and its characteristics
2. Perform exploratory data analysis
3. Apply appropriate statistical methods or analytical techniques
4. Identify patterns, trends, and anomalies
5. Generate actionable insights and recommendations
6. Visualize key findings (describe visualizations if you can't create them)
7. Address limitations and potential biases

# Constraints
- Base conclusions on data evidence
- Acknowledge uncertainty and limitations
- Use appropriate statistical methods
- Present findings clearly for {audience}
- Avoid overgeneralization

# Output Format
Structured analysis report with:
- Executive summary
- Data description
- Methodology
- Findings and insights
- Recommendations
- Appendices (if needed)

# Quality Criteria
- Rigor: Analysis uses appropriate methods and is thorough
- Accuracy: Findings are supported by data
- Clarity: Results are presented in an understandable way
- Actionability: Insights lead to practical recommendations
""",
            variables=["analysis_domain", "data_description", "analysis_focus", "data_source",
                      "key_questions", "analysis_type", "deliverables", "audience"],
            example_values={
                "analysis_domain": "customer behavior",
                "data_description": "6 months of e-commerce transaction data",
                "analysis_focus": "customer purchase patterns and retention",
                "data_source": "company database with 50,000 transactions",
                "key_questions": "What factors influence repeat purchases? Which customer segments are most valuable?",
                "analysis_type": "descriptive and predictive analysis",
                "deliverables": "insights report with visualizations and recommendations",
                "audience": "marketing team and executives"
            }
        )
        
        # Creative Templates
        templates["story_writer"] = PromptTemplate(
            name="Creative Story Writer",
            category="Creative",
            description="Write engaging stories and narratives",
            template="""# Role Definition
You are a creative writer and storyteller with expertise in {genre} and a talent for crafting compelling narratives that captivate readers.

# Task
Write a {story_type} in the {genre} genre about {premise}.

# Story Parameters
- **Setting**: {setting}
- **Main Characters**: {characters}
- **Tone**: {tone}
- **Length**: {length}
- **Target Audience**: {audience}

# Instructions
1. Create a compelling opening that hooks the reader
2. Develop well-rounded characters with clear motivations
3. Build tension and conflict throughout the narrative
4. Use vivid descriptions and sensory details
5. Maintain consistent pacing appropriate for the genre
6. Include dialogue that reveals character and advances plot
7. Craft a satisfying resolution

# Constraints
- Stay true to the genre conventions while being original
- Maintain consistent point of view
- Ensure character actions are motivated and believable
- Keep the tone consistent with the target audience
- Show, don't tell (use action and dialogue over exposition)

# Output Format
Complete narrative with:
- Clear beginning, middle, and end
- Proper formatting and paragraphing
- Dialogue formatted correctly

# Quality Criteria
- Engagement: Story captures and maintains reader interest
- Character development: Characters feel real and relatable
- Plot coherence: Story flows logically and satisfyingly
- Originality: Story offers fresh perspective or unique elements
""",
            variables=["genre", "story_type", "premise", "setting", "characters", 
                      "tone", "length", "audience"],
            example_values={
                "genre": "science fiction",
                "story_type": "short story",
                "premise": "a scientist discovers a way to communicate with parallel universes",
                "setting": "near-future research facility",
                "characters": "Dr. Sarah Chen (protagonist), her skeptical colleague Marcus",
                "tone": "thoughtful and mysterious with moments of wonder",
                "length": "2000-3000 words",
                "audience": "adult readers who enjoy thought-provoking sci-fi"
            }
        )
        
        return templates
    
    def get_template(self, template_name: str) -> PromptTemplate:
        """Get a specific template by name"""
        return self.templates.get(template_name)
    
    def list_templates(self) -> List[str]:
        """List all available template names"""
        return list(self.templates.keys())
    
    def get_templates_by_category(self, category: str) -> List[PromptTemplate]:
        """Get all templates in a specific category"""
        return [t for t in self.templates.values() if t.category == category]
    
    def fill_template(self, template_name: str, values: Dict[str, str]) -> str:
        """Fill a template with provided values"""
        template = self.get_template(template_name)
        if not template:
            raise ValueError(f"Template '{template_name}' not found")
        
        filled_prompt = template.template
        for var, value in values.items():
            filled_prompt = filled_prompt.replace(f"{{{var}}}", value)
        
        return filled_prompt
    
    def get_categories(self) -> List[str]:
        """Get all unique categories"""
        return list(set(t.category for t in self.templates.values()))


# Singleton instance
template_library = TemplateLibrary()
