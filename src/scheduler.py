import asyncio
from datetime import datetime, timezone
from apscheduler.schedulers.asyncio import AsyncIOScheduler


class PostScheduler:
      def __init__(self, db, config):
                self.db = db
                self.config = config
                self._scheduler = AsyncIOScheduler(timezone=config.timezone)

      def start(self):
                self._scheduler.add_job(
                              self._process_queue,
                              "interval",
                              seconds=30,
                              id="queue_processor",
                              replace_existing=True,
                    
