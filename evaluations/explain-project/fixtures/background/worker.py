import json
import os
import time
from urllib.request import Request, urlopen

from store import next_job, get_order, finish_job


def deliver(order):
    request = Request(
        os.environ['NOTIFY_URL'],
        data=json.dumps({'to': order['email'], 'order_id': order['id']}).encode(),
        headers={
            'Authorization': 'Bearer ' + os.environ['NOTIFY_TOKEN'],
            'Content-Type': 'application/json',
        },
        method='POST',
    )
    with urlopen(request, timeout=5) as response:
        if response.status != 200:
            raise RuntimeError('notification rejected')


def tick():
    order_id = next_job()
    if order_id is None:
        return
    try:
        deliver(get_order(order_id))
    except Exception:
        finish_job(order_id, 'failed')
    else:
        finish_job(order_id, 'sent')


if __name__ == '__main__':
    while True:
        tick()
        time.sleep(1)
