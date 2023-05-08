import time

import allure
import pytest

from src.response_objects import TrelloObject, TrelloObjectList
from config import Parameters


@allure.title('Create and delete the new board')
@pytest.fixture()
def new_board(api):
    """Fixture that add board"""
    boards = []

    def add_board(name):
        with allure.step('Create new board'):
            boards.append(TrelloObject(api.post('boards', name=name)))
        return boards[0]

    yield add_board

    with allure.step('Delete created board'):
        api.delete(f'boards/{boards[0].id}')


@pytest.fixture()
def new_list(api):
    """Fixture that add list on the current board"""

    def add_list(board, name):
        list = TrelloObject(api.post('lists', name=name, idBoard=board.id))
        return list

    return add_list


@pytest.fixture()
def get_lists(api):
    """Fixture that return lists of lists on the current board"""

    def get(board):
        list = TrelloObjectList(api.get(f'boards/{board.id}/lists'))
        return list

    return get


@pytest.fixture()
def get_cards(api):
    """Fixture that return cards on the current list"""

    def get(list):
        list = TrelloObjectList(api.get(f'lists/{list.id}/cards'))
        return list

    return get


@pytest.fixture()
def new_list_and_board(new_board, new_list):
    """Fixture that create board and add the list"""
    board_name = f'AT Board {str(time.time())[:-8]}'
    with allure.step('Create new board'):
        new_board = new_board(name=board_name)
    with allure.step('Create new list'):
        new_list = new_list(board=new_board, name=Parameters.default_name)
    return {'board': new_board, 'list': new_list}
