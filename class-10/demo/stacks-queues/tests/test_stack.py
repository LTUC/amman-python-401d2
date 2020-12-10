from stacks_queues.stack import Stack


def test_push_4_items():
    lines = Stack()
    lines.push('hello from class')
    lines.push('welcome to demo')
    lines.push('we learn coding')
    lines.push('bye')
    assert lines.peek() == 'bye'
