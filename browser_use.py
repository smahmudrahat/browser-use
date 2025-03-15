"""Wrapper for browser-use agent."""
import os
import sys
from typing import Any, Dict
from datetime import datetime
from ..base_agent import BaseAgent

# Add parent directory to Python path to find browser_use_main
parent_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if parent_dir not in sys.path:
    sys.path.append(parent_dir)

from browser_use_main import Agent as BrowserUseBaseAgent

class Agent(BaseAgent):
    """Wrapper for browser-use agent."""
    
    def __init__(self, task: str, **kwargs):
        """Initialize the browser-use agent.
        
        Args:
            task (str): The task description/prompt
            **kwargs: Additional parameters including:
                - start_url (str): Starting URL for browser
        """
        super().__init__(task, **kwargs)
        # Only pass supported parameters to browser-use agent
        browser_kwargs = {}
        if 'start_url' in kwargs:
            browser_kwargs['start_url'] = kwargs['start_url']
            
        self.agent = BrowserUseBaseAgent(**browser_kwargs)
        
    async def run(self) -> Any:
        """Execute the task using browser-use agent.
        
        Returns:
            Any: The result of task execution, with methods:
                - final_result(): str
                - number_of_steps(): int
                - total_duration_seconds(): float
                - total_input_tokens(): int
        """
        start_time = datetime.now()
        result = await self.agent.run(self.task)
        # Browser-use agent already returns an object with these methods
        return result 