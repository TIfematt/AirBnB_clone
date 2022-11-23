#!/usr/bin/python3
"""Defines the Review class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represent a review."""

    user_id = ""
    place_id = ""
    text = ""