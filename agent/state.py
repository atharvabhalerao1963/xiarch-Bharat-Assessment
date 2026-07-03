"""
In this module its give what is the current State of my workflow 

Defines the shared workflow state for the Autonomous Research Agent.
The WorkflowState acts as the single source of truth during the
research process. Each module reads from and updates this object
instead of passing multiple variables between functions.
"""

from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field

from models.schemas import (
    UserQuery,
    ResearchPlan,
    SearchResult,
    SourceDocument,
    ResearchReport,
)


class WorkflowState(BaseModel):
    """
    Stores the current state of the research workflow.
    """

    # User input
    user_query: Optional[UserQuery] = None

    # Planning
    research_plan: Optional[ResearchPlan] = None

    # Selected search providers
    selected_sources: List[str] = Field(default_factory=list)

    # Search results
    search_results: List[SearchResult] = Field(default_factory=list)

    # Extracted documents
    documents: List[SourceDocument] = Field(default_factory=list)

    # Processed documents
    clean_documents: List[SourceDocument] = Field(default_factory=list)

    relevant_documents: List[SourceDocument] = Field(default_factory=list)

    # Context prepared for the LLM
    context: Optional[str] = None

    # Final report
    report: Optional[ResearchReport] = None

    # Workflow information
    current_stage: str = "Initialized"

    errors: List[str] = Field(default_factory=list)

    created_at: datetime = Field(default_factory=datetime.utcnow)