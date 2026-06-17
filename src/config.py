import os
from functools import lru_cache
from dataclasses import dataclass, field
from typing import Any

import yaml


@dataclass
class DatabaseConfig:
      driver: str = "sqlite"
      path: str = "data/contentflow.db"
      pool_size: int = 5


@dataclass
class SchedulerConfig:
      timezone: str = "UTC"
      max_queue_size: int = 500
      retry_on_failure: bool = True
      retry_delay_seconds: int = 120


@dataclass
class Settings:
      database: DatabaseConfig = field(default_factory=DatabaseConfig)
