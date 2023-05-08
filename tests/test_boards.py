import pytest
import time
from allure import feature, step, story, title
from hamcrest import (assert_that, equal_to, greater_than)
from src.response_objects import TrelloObjectList
from config import Parameters


@title('Get all user boards')
@pytest.fixture()
def all_boards(api):
    """Fixture that creates new board"""
    with step('Get all boards'):
        return TrelloObjectList(api.get('members/me/boards'))


@feature('Trello testing')
@story('Boards')
class TestBoards:
    @title('Board creation')
    def test_create_new_board(self, new_board):
        board_name = f'AT Board {str(time.time())[:-8]}'
        with step('Create new board'):
            new_board = new_board(name=board_name)
        with step('Assert that new board was created'):
            assert_that(new_board.name, equal_to(board_name))

    @title('Board collection')
    def test_get_all_boards(self, all_boards):
        with step('Assert that users contains more then 2 boards'):
            assert_that(all_boards.count, greater_than(2))

    @title('Get count of lists on new board')
    def test_default_list_count_from_board(self, new_board, get_lists):
        board_name = f'AT Board {str(time.time())[:-8]}'
        with step('Create new board'):
            new_board = new_board(name=board_name)
        with step('Assert that new board has 3 lists by default'):
            lists_on_board = get_lists(new_board)
            assert_that(lists_on_board.count, equal_to(Parameters.default_list_count))
