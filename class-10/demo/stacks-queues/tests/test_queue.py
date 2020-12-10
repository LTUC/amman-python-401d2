from stacks_queues.queue import Queue
import pytest

def test_enqueue_3_items(prep_queue):
    assert prep_queue.peek() == 3



@pytest.fixture
def prep_queue():
    queue = Queue()
    queue.enqueue(3)
    queue.enqueue(5)
    queue.enqueue('hello')
    return queue
