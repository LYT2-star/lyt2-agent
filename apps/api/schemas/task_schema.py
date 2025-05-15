# apps/api/schemas/task_schema.py

from pydantic import BaseModel
from typing import Dict, Optional

class TaskSubmitResponse(BaseModel):
    parsed: Optional[Dict] = None
    score: Optional[Dict] = None
    report_url: Optional[str] = None

