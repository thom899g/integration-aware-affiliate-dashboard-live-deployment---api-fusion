"""
Flask API Bridge for Evolution Ecosystem
Connects the Firebase-hosted dashboard with Python backend optimization engine.
Provides secure REST API endpoints for real-time data exchange.
"""
import os
import sys
import json
import logging
import traceback
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional, Tuple
from pathlib import Path

# Third-party imports
from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
import firebase_admin
from firebase_admin import credentials, firestore, auth
import pandas as pd
import numpy as np
from dataclasses import dataclass, asdict
from enum import Enum

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(module)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize Flask app
app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": ["https://evolution-ecosystem.web.app", "http://localhost:5000"]}})

# Configuration
class Config:
    """Application configuration."""
    DEBUG = os.getenv('FLASK_DEBUG', 'False').lower() == 'true'
    PORT = int(os