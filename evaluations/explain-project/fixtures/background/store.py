import os
import sqlite3
from uuid import uuid4


def connect():
    db = sqlite3.connect(os.environ.get('ORDER_DB', 'orders.sqlite3'))
    db.row_factory = sqlite3.Row
    return db


def initialize():
    with connect() as db:
        db.executescript('''
            CREATE TABLE IF NOT EXISTS orders (
                id TEXT PRIMARY KEY, item TEXT NOT NULL, email TEXT NOT NULL,
                notification_status TEXT NOT NULL
            );
            CREATE TABLE IF NOT EXISTS jobs (
                order_id TEXT PRIMARY KEY, status TEXT NOT NULL
            );
        ''')


def create_order(item, email):
    order_id = str(uuid4())
    with connect() as db:
        db.execute('INSERT INTO orders VALUES (?, ?, ?, ?)',
                   (order_id, item, email, 'pending'))
        db.execute('INSERT INTO jobs VALUES (?, ?)', (order_id, 'pending'))
    return get_order(order_id)


def get_order(order_id):
    with connect() as db:
        row = db.execute('SELECT * FROM orders WHERE id = ?', (order_id,)).fetchone()
    return dict(row) if row else None


def next_job():
    with connect() as db:
        row = db.execute("SELECT order_id FROM jobs WHERE status = 'pending' LIMIT 1").fetchone()
    return row['order_id'] if row else None


def finish_job(order_id, status):
    with connect() as db:
        db.execute('UPDATE jobs SET status = ? WHERE order_id = ?', (status, order_id))
        db.execute('UPDATE orders SET notification_status = ? WHERE id = ?',
                   (status, order_id))
