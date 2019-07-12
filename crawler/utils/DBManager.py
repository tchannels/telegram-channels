import sqlite3
import logging

logger = logging.getLogger('channels_crawler')

class DBManager:
    def __init__(self):
        self.connection = sqlite3.connect('data.db')
        
        cursor = self.connection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS "channels" (
                "id" INTEGER PRIMARY KEY,
                "channel_id" TEXT NOT NULL UNIQUE,
                "title" TEXT,
                "image_link" TEXT,
                "description" TEXT
            );
        ''')
        self.connection.commit()

    def save_channel(self, data:dict):
        logger.debug('Saving channel with data: %s' % data)
        cursor = self.connection.cursor()
        params = [data.get(x) for x in ('channel_id', 'title', 'image_link', 'description')]
        cursor.execute('''
            INSERT INTO "channels" ("channel_id", "title", "image_link", "description")
            VALUES (?, ?, ?, ?)
        ''', params)
        self.connection.commit()

    def __del__(self):
        self.connection.close()
