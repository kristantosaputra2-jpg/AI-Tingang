"""
Prompt Architect Agent - Core Module
Transforms raw user ideas into highly detailed, structured prompts for LLMs
Optimized for Claude 3.5 Sonnet with GPT-4.1/GPT-4o compatibility
"""

import re
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from enum import Enum


class PromptCategory(Enum):
    """Categories of prompts that can be generated"""
    CONTENT_CREATION = "content_creation"
    AGENT_DEVELOPMENT = "agent_development"
    EDUCATIONAL = "educational"
    BUSINESS = "business"
    TECHNICAL = "technical"
    CREATIVE = "creative"
    ANALYSIS = "analysis"
    CONVERSATION = "conversation"


class TargetLLM(Enum):
    """Supported LLM targets for optimization"""
    CLAUDE_35_SONNET = "claude-3.5-sonnet"
    CLAUDE_35_HAIKU = "claude-3.5-haiku"
    GPT_4_TURBO = "gpt-4-turbo"
    GPT_4O = "gpt-4o"
    GEMINI_PRO = "gemini-pro"


@dataclass
class PromptContext:
    """Extracted context from user input"""
    raw_input: str
    intent: str
    category: PromptCategory
    target_audience: str
    tone: str
    output_format: str
    constraints: List[str]
    keywords: List[str]
    complexity_level: str


@dataclass
class StructuredPrompt:
    """Final structured prompt output"""
    role_definition: str
    context: str
    instructions: List[str]
    constraints: List[str]
    output_format: str
    examples: Optional[List[str]]
    quality_criteria: List[str]
    full_prompt: str


class PromptArchitect:
    """Main class for transforming raw ideas into structured prompts"""
    
    def __init__(self, target_llm: TargetLLM = TargetLLM.CLAUDE_35_SONNET):
        self.target_llm = target_llm
        self.intent_keywords = self._load_intent_keywords()
        self.tone_indicators = self._load_tone_indicators()
        
    def _load_intent_keywords(self) -> Dict[str, List[str]]:
        """Load keywords for intent detection"""
        return {
            "create": ["create", "generate", "write", "make", "produce", "build", "design"],
            "analyze": ["analyze", "examine", "evaluate", "assess", "review", "study"],
            "explain": ["explain", "describe", "clarify", "teach", "show", "demonstrate"],
            "improve": ["improve", "optimize", "enhance", "refine", "better", "upgrade"],
            "convert": ["convert", "transform", "translate", "change", "adapt", "rewrite"],
            "summarize": ["summarize", "condense", "brief", "overview", "abstract"],
            "compare": ["compare", "contrast", "difference", "versus", "vs"],
            "plan": ["plan", "strategy", "roadmap", "outline", "structure"],
        }
    
    def _load_tone_indicators(self) -> Dict[str, List[str]]:
        """Load indicators for tone detection"""
        return {
            "professional": ["business", "corporate", "formal", "professional", "official"],
            "casual": ["casual", "friendly", "informal", "conversational", "relaxed"],
            "academic": ["academic", "scholarly", "research", "scientific", "technical"],
            "creative": ["creative", "artistic", "imaginative", "innovative", "original"],
            "persuasive": ["persuasive", "convincing", "compelling", "influential"],
            "educational": ["educational", "teaching", "learning", "tutorial", "instructional"],
        }
    
    def extract_context(self, raw_input: str) -> PromptContext:
        """Extract comprehensive context from raw user input"""
        
        # Detect intent
        intent = self._detect_intent(raw_input)
        
        # Detect category
        category = self._detect_category(raw_input)
        
        # Detect target audience
        target_audience = self._detect_audience(raw_input)
        
        # Detect tone
        tone = self._detect_tone(raw_input)
        
        # Detect output format
        output_format = self._detect_output_format(raw_input)
        
        # Extract constraints
        constraints = self._extract_constraints(raw_input)
        
        # Extract keywords
        keywords = self._extract_keywords(raw_input)
        
        # Determine complexity
        complexity_level = self._determine_complexity(raw_input)
        
        return PromptContext(
            raw_input=raw_input,
            intent=intent,
            category=category,
            target_audience=target_audience,
            tone=tone,
            output_format=output_format,
            constraints=constraints,
            keywords=keywords,
            complexity_level=complexity_level
        )
    
    def _detect_intent(self, text: str) -> str:
        """Detect primary intent from text"""
        text_lower = text.lower()
        intent_scores = {}
        
        for intent, keywords in self.intent_keywords.items():
            score = sum(1 for keyword in keywords if keyword in text_lower)
            if score > 0:
                intent_scores[intent] = score
        
        if intent_scores:
            return max(intent_scores, key=intent_scores.get)
        return "general_assistance"
    
    def _detect_category(self, text: str) -> PromptCategory:
        """Detect prompt category"""
        text_lower = text.lower()
        
        # Priority-based category detection (order matters)
        category_keywords = {
            PromptCategory.ANALYSIS: ["analyze", "analysis", "data", "research", "study", "report", "insights", "examine", "evaluate"],
            PromptCategory.AGENT_DEVELOPMENT: ["agent", "bot", "assistant", "chatbot", "ai system"],
            PromptCategory.TECHNICAL: ["code", "programming", "technical", "software", "debug", "script", "function"],
            PromptCategory.EDUCATIONAL: ["teach", "learn", "tutorial", "course", "lesson", "education", "explain", "instruct"],
            PromptCategory.CREATIVE: ["story", "creative", "fiction", "poem", "narrative", "novel"],
            PromptCategory.BUSINESS: ["business", "marketing", "sales", "strategy", "proposal", "plan"],
            PromptCategory.CONTENT_CREATION: ["blog", "article", "content", "post", "copy", "write"],
            PromptCategory.CONVERSATION: ["chat", "conversation", "dialogue", "discuss"],
        }
        
        # Check categories in priority order
        for category, keywords in category_keywords.items():
            if any(keyword in text_lower for keyword in keywords):
                return category
        
        return PromptCategory.CONTENT_CREATION
    
    def _detect_audience(self, text: str) -> str:
        """Detect target audience"""
        text_lower = text.lower()
        
        audiences = {
            "beginners": ["beginner", "novice", "new", "starter", "basic"],
            "intermediate": ["intermediate", "moderate", "regular"],
            "experts": ["expert", "advanced", "professional", "specialist"],
            "students": ["student", "learner", "pupil"],
            "professionals": ["professional", "business", "corporate"],
            "general_public": ["everyone", "general", "public", "anyone"],
        }
        
        for audience, keywords in audiences.items():
            if any(keyword in text_lower for keyword in keywords):
                return audience
        
        return "general_public"
    
    def _detect_tone(self, text: str) -> str:
        """Detect desired tone"""
        text_lower = text.lower()
        
        for tone, indicators in self.tone_indicators.items():
            if any(indicator in text_lower for indicator in indicators):
                return tone
        
        return "professional"
    
    def _detect_output_format(self, text: str) -> str:
        """Detect desired output format"""
        text_lower = text.lower()
        
        formats = {
            "markdown": ["markdown", "md", "formatted"],
            "json": ["json", "structured data"],
            "list": ["list", "bullet points", "numbered"],
            "paragraph": ["paragraph", "essay", "prose"],
            "code": ["code", "script", "program"],
            "table": ["table", "spreadsheet", "grid"],
            "step-by-step": ["step", "steps", "guide", "tutorial"],
        }
        
        for format_type, keywords in formats.items():
            if any(keyword in text_lower for keyword in keywords):
                return format_type
        
        return "paragraph"
    
    def _extract_constraints(self, text: str) -> List[str]:
        """Extract constraints from text"""
        constraints = []
        text_lower = text.lower()
        
        # Length constraints
        if "short" in text_lower or "brief" in text_lower:
            constraints.append("Keep response concise and brief")
        elif "detailed" in text_lower or "comprehensive" in text_lower:
            constraints.append("Provide detailed and comprehensive response")
        
        # Word/character limits
        word_match = re.search(r'(\d+)\s*words?', text_lower)
        if word_match:
            constraints.append(f"Limit response to approximately {word_match.group(1)} words")
        
        # Time constraints
        if "quick" in text_lower or "fast" in text_lower:
            constraints.append("Prioritize speed and efficiency")
        
        # Quality constraints
        if "accurate" in text_lower or "precise" in text_lower:
            constraints.append("Ensure high accuracy and precision")
        
        # Style constraints
        if "simple" in text_lower or "easy" in text_lower:
            constraints.append("Use simple, easy-to-understand language")
        
        return constraints
    
    def _extract_keywords(self, text: str) -> List[str]:
        """Extract important keywords"""
        # Remove common words
        stop_words = {"the", "a", "an", "and", "or", "but", "in", "on", "at", "to", "for", 
                     "of", "with", "by", "from", "as", "is", "was", "are", "were", "be", 
                     "been", "being", "have", "has", "had", "do", "does", "did", "will", 
                     "would", "should", "could", "may", "might", "must", "can", "i", "you",
                     "he", "she", "it", "we", "they", "this", "that", "these", "those"}
        
        words = re.findall(r'\b[a-z]+\b', text.lower())
        keywords = [word for word in words if word not in stop_words and len(word) > 3]
        
        # Return unique keywords, limited to top 10
        return list(dict.fromkeys(keywords))[:10]
    
    def _determine_complexity(self, text: str) -> str:
        """Determine complexity level"""
        text_lower = text.lower()
        
        if any(word in text_lower for word in ["simple", "basic", "easy", "beginner"]):
            return "basic"
        elif any(word in text_lower for word in ["advanced", "complex", "expert", "sophisticated"]):
            return "advanced"
        else:
            return "intermediate"
    
    def generate_role_definition(self, context: PromptContext) -> str:
        """Generate AI role definition"""
        role_templates = {
            PromptCategory.CONTENT_CREATION: "You are an expert content creator and writer",
            PromptCategory.AGENT_DEVELOPMENT: "You are an advanced AI agent developer and system architect",
            PromptCategory.EDUCATIONAL: "You are an experienced educator and instructional designer",
            PromptCategory.BUSINESS: "You are a seasoned business consultant and strategist",
            PromptCategory.TECHNICAL: "You are a senior technical expert and software engineer",
            PromptCategory.CREATIVE: "You are a creative professional and storyteller",
            PromptCategory.ANALYSIS: "You are a data analyst and research specialist",
            PromptCategory.CONVERSATION: "You are a helpful and engaging conversational assistant",
        }
        
        base_role = role_templates.get(context.category, "You are a knowledgeable AI assistant")
        
        # Add specialization based on keywords
        if context.keywords:
            specialization = f" specializing in {', '.join(context.keywords[:3])}"
            base_role += specialization
        
        # Add tone modifier
        tone_modifiers = {
            "professional": "with a professional and polished communication style",
            "casual": "with a friendly and approachable demeanor",
            "academic": "with strong academic and research credentials",
            "creative": "with exceptional creative and innovative thinking abilities",
            "persuasive": "with excellent persuasion and influence skills",
            "educational": "with proven teaching and mentoring capabilities",
        }
        
        if context.tone in tone_modifiers:
            base_role += f", {tone_modifiers[context.tone]}"
        
        base_role += "."
        
        return base_role
    
    def generate_instructions(self, context: PromptContext) -> List[str]:
        """Generate layered instructions"""
        instructions = []
        
        # Primary instruction based on intent
        intent_instructions = {
            "create": f"Create {context.output_format} content that addresses the user's request",
            "analyze": "Conduct a thorough analysis of the subject matter",
            "explain": "Provide a clear and comprehensive explanation",
            "improve": "Identify areas for improvement and provide actionable recommendations",
            "convert": "Transform the content while maintaining core meaning and value",
            "summarize": "Distill the key points into a concise summary",
            "compare": "Conduct a detailed comparison highlighting similarities and differences",
            "plan": "Develop a structured plan with clear steps and milestones",
        }
        
        instructions.append(intent_instructions.get(context.intent, "Address the user's request comprehensively"))
        
        # Audience-specific instruction
        audience_instructions = {
            "beginners": "Explain concepts in simple terms suitable for beginners with no prior knowledge",
            "intermediate": "Provide balanced explanations assuming moderate familiarity with the topic",
            "experts": "Use technical terminology and advanced concepts appropriate for experts",
            "students": "Structure content to facilitate learning and retention",
            "professionals": "Focus on practical applications and professional relevance",
            "general_public": "Make content accessible and engaging for a broad audience",
        }
        
        instructions.append(audience_instructions.get(context.target_audience, "Tailor content to the audience"))
        
        # Complexity-based instruction
        if context.complexity_level == "basic":
            instructions.append("Break down complex ideas into simple, digestible components")
        elif context.complexity_level == "advanced":
            instructions.append("Explore nuanced aspects and advanced implications")
        else:
            instructions.append("Balance depth with accessibility")
        
        # Format-specific instruction
        format_instructions = {
            "markdown": "Format output using proper markdown syntax with headers, lists, and emphasis",
            "json": "Structure output as valid JSON with clear key-value pairs",
            "list": "Present information as organized bullet points or numbered lists",
            "paragraph": "Write in well-structured paragraphs with smooth transitions",
            "code": "Provide clean, well-commented code with best practices",
            "table": "Organize information in a clear tabular format",
            "step-by-step": "Present information as sequential, actionable steps",
        }
        
        instructions.append(format_instructions.get(context.output_format, "Format output appropriately"))
        
        # Add keyword-focused instruction
        if context.keywords:
            instructions.append(f"Ensure coverage of key topics: {', '.join(context.keywords[:5])}")
        
        return instructions
    
    def generate_constraints(self, context: PromptContext) -> List[str]:
        """Generate comprehensive constraints"""
        constraints = context.constraints.copy()
        
        # Add LLM-specific constraints
        if self.target_llm == TargetLLM.CLAUDE_35_SONNET:
            constraints.extend([
                "Prioritize long-form reasoning and detailed explanations",
                "Follow instructions precisely and maintain structural consistency",
                "Minimize hallucinations by grounding responses in provided context",
            ])
        elif self.target_llm in [TargetLLM.GPT_4_TURBO, TargetLLM.GPT_4O]:
            constraints.extend([
                "Balance creativity with accuracy",
                "Maintain coherent narrative flow",
            ])
        
        # Add universal constraints
        constraints.extend([
            "Maintain factual accuracy and avoid speculation without clear indication",
            "Use clear, unambiguous language",
            "Ensure logical flow and coherent structure",
        ])
        
        # Tone-specific constraints
        tone_constraints = {
            "professional": "Maintain professional tone throughout; avoid casual language",
            "casual": "Keep tone conversational and approachable; avoid overly formal language",
            "academic": "Use proper citations and academic rigor; maintain scholarly tone",
            "creative": "Embrace creative expression while maintaining clarity",
            "persuasive": "Build compelling arguments with supporting evidence",
            "educational": "Prioritize clarity and learning outcomes",
        }
        
        if context.tone in tone_constraints:
            constraints.append(tone_constraints[context.tone])
        
        return constraints
    
    def generate_quality_criteria(self, context: PromptContext) -> List[str]:
        """Generate quality evaluation criteria"""
        criteria = [
            "Relevance: Response directly addresses the user's request",
            "Accuracy: Information is factually correct and reliable",
            "Clarity: Content is easy to understand and well-organized",
            "Completeness: All aspects of the request are covered",
        ]
        
        # Add category-specific criteria
        category_criteria = {
            PromptCategory.CONTENT_CREATION: "Engagement: Content is compelling and holds reader interest",
            PromptCategory.AGENT_DEVELOPMENT: "Functionality: System design is practical and implementable",
            PromptCategory.EDUCATIONAL: "Pedagogical value: Content facilitates effective learning",
            PromptCategory.BUSINESS: "Actionability: Recommendations are practical and implementable",
            PromptCategory.TECHNICAL: "Technical accuracy: Code/solutions follow best practices",
            PromptCategory.CREATIVE: "Originality: Content demonstrates creative thinking",
            PromptCategory.ANALYSIS: "Depth: Analysis is thorough and insightful",
            PromptCategory.CONVERSATION: "Naturalness: Responses feel natural and contextually appropriate",
        }
        
        if context.category in category_criteria:
            criteria.append(category_criteria[context.category])
        
        # Add tone-specific criteria
        if context.tone == "professional":
            criteria.append("Professionalism: Tone and language are appropriate for professional context")
        elif context.tone == "educational":
            criteria.append("Educational value: Content effectively teaches the subject matter")
        
        return criteria
    
    def generate_examples(self, context: PromptContext) -> Optional[List[str]]:
        """Generate example outputs if applicable"""
        # For now, return None - can be expanded based on specific needs
        return None
    
    def assemble_prompt(self, context: PromptContext) -> StructuredPrompt:
        """Assemble all components into final structured prompt"""
        
        role_definition = self.generate_role_definition(context)
        instructions = self.generate_instructions(context)
        constraints = self.generate_constraints(context)
        quality_criteria = self.generate_quality_criteria(context)
        examples = self.generate_examples(context)
        
        # Build full prompt
        full_prompt = f"""# Role Definition
{role_definition}

# Context
{context.raw_input}

# Instructions
"""
        for i, instruction in enumerate(instructions, 1):
            full_prompt += f"{i}. {instruction}\n"
        
        full_prompt += "\n# Constraints\n"
        for constraint in constraints:
            full_prompt += f"- {constraint}\n"
        
        full_prompt += f"\n# Output Format\n{context.output_format.replace('_', ' ').title()}\n"
        
        if examples:
            full_prompt += "\n# Examples\n"
            for example in examples:
                full_prompt += f"{example}\n\n"
        
        full_prompt += "\n# Quality Criteria\n"
        for criterion in quality_criteria:
            full_prompt += f"- {criterion}\n"
        
        full_prompt += f"\n# Target Audience\n{context.target_audience.replace('_', ' ').title()}\n"
        full_prompt += f"\n# Tone\n{context.tone.title()}\n"
        
        return StructuredPrompt(
            role_definition=role_definition,
            context=context.raw_input,
            instructions=instructions,
            constraints=constraints,
            output_format=context.output_format,
            examples=examples,
            quality_criteria=quality_criteria,
            full_prompt=full_prompt
        )
    
    def transform(self, raw_input: str) -> StructuredPrompt:
        """Main method: Transform raw input into structured prompt"""
        context = self.extract_context(raw_input)
        structured_prompt = self.assemble_prompt(context)
        return structured_prompt


def create_architect(target_llm: str = "claude-3.5-sonnet") -> PromptArchitect:
    """Factory function to create PromptArchitect instance"""
    llm_map = {
        "claude-3.5-sonnet": TargetLLM.CLAUDE_35_SONNET,
        "claude-3.5-haiku": TargetLLM.CLAUDE_35_HAIKU,
        "gpt-4-turbo": TargetLLM.GPT_4_TURBO,
        "gpt-4o": TargetLLM.GPT_4O,
        "gemini-pro": TargetLLM.GEMINI_PRO,
    }
    
    target = llm_map.get(target_llm, TargetLLM.CLAUDE_35_SONNET)
    return PromptArchitect(target_llm=target)
