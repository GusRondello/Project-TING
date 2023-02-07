import pytest
from ting_file_management.priority_queue import PriorityQueue


mocked_big_file = {
    "nome_do_arquivo": "Mocked_Big",
    "qtd_linhas": 8,
    "linhas_do_arquivo": ["Eight Lines"],
}

mocked_small_file = {
    "nome_do_arquivo": "Mocked_Small",
    "qtd_linhas": 2,
    "linhas_do_arquivo": ["Two Lines"],
}


def test_basic_priority_queueing():
    __test_len()
    __test_search()
    __test_search_error()
    __test_dequeue()


def __test_len():
    p_queue = PriorityQueue()
    p_queue.enqueue(mocked_big_file)
    p_queue.enqueue(mocked_small_file)
    assert p_queue.high_priority.__len__() == 1
    assert p_queue.regular_priority.__len__() == 1


def __test_search():
    p_queue = PriorityQueue()
    p_queue.enqueue(mocked_big_file)
    p_queue.enqueue(mocked_small_file)
    search = p_queue.search(0)
    assert search == mocked_small_file


def __test_search_error():
    p_queue = PriorityQueue()
    p_queue.enqueue(mocked_big_file)
    p_queue.enqueue(mocked_small_file)
    with pytest.raises(IndexError):
        p_queue.search(3)


def __test_dequeue():
    p_queue = PriorityQueue()
    p_queue.enqueue(mocked_big_file)
    p_queue.enqueue(mocked_small_file)
    remove = p_queue.dequeue()
    assert remove == mocked_small_file
