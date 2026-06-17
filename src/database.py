import os
import aiosqlite
from datetime import datetime, timezone


class Database:
      def __init__(self, config):
                self.path = config.path
                self._conn = None

      async def initialize(self):
                os.makedirs(os.path.dirname(self.path) or ".", exist_ok=True)
                self._conn = await aiosqlite.connect(self.path)
                self._conn.row_factory = aiosqlite.Row
                await self._conn.executescript(SCHEMA)

      async def close(self):
                if self._conn:
                              await sel
