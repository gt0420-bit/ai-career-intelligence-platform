import asyncio
import json
import logging
from datetime import datetime, timedelta
from typing import Dict, List, Any
from dataclasses import dataclass
import uuid
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class AgentResult:
    success: bool
    data: Dict[str, Any]
    confidence_score: float
    execution_time: float
    errors: List[str] = None
    recommendations: List[str] = None

class BaseAgent:
    def __init__(self, agent_role: str, config: Dict[str, Any] = None):
        self.agent_role = agent_role
        self.agent_id = str(uuid.uuid4())
        self.config = config or {}
        self.is_active = True
        self.stats = {
            'tasks_completed': 0,
            'tasks_failed': 0,
            'last_heartbeat': datetime.utcnow()
        }
    
    async def execute_task(self, task_data: Dict[str, Any]) -> AgentResult:
        """Override this method in specific agents"""
        raise NotImplementedError
    
    async def generate_autonomous_tasks(self, user_id: int) -> List[Dict[str, Any]]:
        """Override this method in specific agents"""
        raise NotImplementedError
    
    def log_info(self, message: str):
        logger.info(f"[{self.agent_role}] {message}")
    
    def log_error(self, message: str):
        logger.error(f"[{self.agent_role}] {message}")
