"""Pydantic models for builder-signal-harvester."""

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, HttpUrl, field_validator


class SocialLinks(BaseModel):
    """Social media and web links."""
    linkedin: Optional[HttpUrl] = None
    twitter: Optional[HttpUrl] = None
    github: Optional[HttpUrl] = None
    website: Optional[HttpUrl] = None


class Evidence(BaseModel):
    """Evidence snippet from a data source."""
    source: str  # "github", "producthunt", etc.
    text: str  # Human-readable evidence
    url: HttpUrl  # Source URL
    timestamp: str  # ISO date or timestamp

    @field_validator('timestamp')
    @classmethod
    def validate_timestamp(cls, v: str) -> str:
        """Validate that timestamp is in ISO format."""
        try:
            datetime.fromisoformat(v.replace('Z', '+00:00'))
        except ValueError:
            raise ValueError(f"timestamp must be in ISO format, got: {v}")
        return v


class Person(BaseModel):
    """Represents a potential operator-angel lead."""
    person_id: str  # Unique identifier
    name: str
    primary_url: HttpUrl
    sources: list[str]  # ["github", "producthunt"]
    operator_score: float = Field(ge=0.0, le=1.0)
    angel_score: float = Field(ge=0.0, le=1.0)
    evidence: list[Evidence] = Field(default_factory=list)
    social_links: Optional[SocialLinks] = None
    last_activity: Optional[str] = None  # ISO date
    canonical_id: Optional[str] = None  # For deduplication

    @field_validator('last_activity')
    @classmethod
    def validate_last_activity(cls, v: Optional[str]) -> Optional[str]:
        """Validate that last_activity is in ISO format if provided."""
        if v is None:
            return v
        try:
            datetime.fromisoformat(v.replace('Z', '+00:00'))
        except ValueError:
            raise ValueError(f"last_activity must be in ISO format, got: {v}")
        return v


class RawProfile(BaseModel):
    """Raw profile data from a harvester before scoring."""
    source: str
    source_id: str  # Username, user ID, etc.
    name: str
    bio: Optional[str] = None
    profile_url: HttpUrl
    social_links: Optional[SocialLinks] = None
    metadata: dict = Field(default_factory=dict)  # Source-specific data
