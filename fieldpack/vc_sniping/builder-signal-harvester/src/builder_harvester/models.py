"""Pydantic models for builder-signal-harvester."""

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field


class SocialLinks(BaseModel):
    """Social media and web links."""
    linkedin: Optional[str] = None
    twitter: Optional[str] = None
    github: Optional[str] = None
    website: Optional[str] = None


class Evidence(BaseModel):
    """Evidence snippet from a data source."""
    source: str  # "github", "producthunt", etc.
    text: str  # Human-readable evidence
    url: str  # Source URL
    timestamp: str  # ISO date or timestamp


class Person(BaseModel):
    """Represents a potential operator-angel lead."""
    person_id: str  # Unique identifier
    name: str
    primary_url: str
    sources: list[str]  # ["github", "producthunt"]
    operator_score: float = Field(ge=0.0, le=1.0)
    angel_score: float = Field(ge=0.0, le=1.0)
    evidence: list[Evidence] = Field(default_factory=list)
    social_links: Optional[SocialLinks] = None
    last_activity: Optional[str] = None  # ISO date
    canonical_id: Optional[str] = None  # For deduplication


class RawProfile(BaseModel):
    """Raw profile data from a harvester before scoring."""
    source: str
    source_id: str  # Username, user ID, etc.
    name: str
    bio: Optional[str] = None
    profile_url: str
    social_links: Optional[SocialLinks] = None
    metadata: dict = Field(default_factory=dict)  # Source-specific data
