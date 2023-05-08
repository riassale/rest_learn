import pytest
import time
from allure import feature, step, story, title
from hamcrest import (assert_that, equal_to, not_none)
from src.response_objects import TrelloObject
from config import Parameters


@pytest.fixture()
def archive_list(api):
    """Fixture that archivate list on the current board"""

    def put(list):
        return TrelloObject(api.put(f'lists/{list.id}/closed', value='true'))

    return put


@pytest.fixture()
def unarchive_list(api):
    """Fixture that unarchivate list on the current board"""

    def put(list):
        return TrelloObject(api.put(f'lists/{list.id}/closed', value='false'))

    return put


@feature('Trello testing')
@story('Lists')
class TestLists:
    @title('List creation')
    def test_create_list(self, new_list_and_board):
        with step('Assert that new list has id and proper name'):
            assert_that(new_list_and_board['list'].id, not_none())
            assert_that(new_list_and_board['list'].name, equal_to(Parameters.default_name))

    @title('Get count of lists after adding the new one')
    def test_get_lists_from_board(self, new_list_and_board, get_lists):
        with step('Assert that the board has 4 lists after creating new list'):
            lists_on_board = get_lists(new_list_and_board['board'])
            assert_that(lists_on_board.count, equal_to(Parameters.default_list_count + 1))

    @title('Get Cards in the New List')
    def test_get_default_cards_count_from_list(self, new_list_and_board, get_cards):
        with step('Assert that list on new board is empty by default'):
            lists_on_board = get_cards(new_list_and_board['list'])
            assert_that(lists_on_board.count, equal_to(0))

    @title('Archiving list')
    def test_archive_list(self, new_list_and_board, archive_list, get_lists):
        with step('Archive one list'):
            archive_list(new_list_and_board['list'])
        with step('Assert that the board has the same count of lists as start count'):
            lists_on_board = get_lists(new_list_and_board['board'])
            assert_that(lists_on_board.count, equal_to(Parameters.default_list_count))

    @title('Unarchiving list')
    def test_unarchiving_list(self, new_list_and_board, archive_list, unarchive_list, get_lists):
        with step('Archive one list'):
            archive_list(new_list_and_board['list'])
            unarchive_list(new_list_and_board['list'])
        with step('Assert that the board has one more list'):
            lists_on_board = get_lists(new_list_and_board['board'])
            assert_that(lists_on_board.count, equal_to(Parameters.default_list_count + 1))
