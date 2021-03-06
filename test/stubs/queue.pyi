# Stubs for queue (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

class Empty(Exception): ...
class Full(Exception): ...

class Queue:
    maxsize = ...  # type: Any
    mutex = ...  # type: Any
    not_empty = ...  # type: Any
    not_full = ...  # type: Any
    all_tasks_done = ...  # type: Any
    unfinished_tasks = ...  # type: Any
    def __init__(self, maxsize: int = 0) -> None: ...
    def task_done(self): ...
    def join(self): ...
    def qsize(self): ...
    def empty(self): ...
    def full(self): ...
    def put(self, item, block=True, timeout=None): ...
    def get(self, block=True, timeout=None): ...
    def put_nowait(self, item): ...
    def get_nowait(self): ...

class PriorityQueue(Queue): ...
class LifoQueue(Queue): ...
