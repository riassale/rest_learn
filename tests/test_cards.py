import pytest
import time
from allure import feature, step, story, title
from hamcrest import (assert_that, equal_to, not_none)
from src.response_objects import TrelloObject
from config import Parameters


@pytest.fixture()
def new_card(api):
    """Fixture that add card on the current list"""

    def add(list, name):
        card = TrelloObject(api.post('cards', name=name, idList=list.id))
        return card

    return add


@feature('Trello testing')
@story('Cards')
class TestCards:
    @title('Cards creation')
    def test_create_card(self, new_list_and_board, new_card):
        with step('Create new card'):
            new_card = new_card(list=new_list_and_board['list'], name=Parameters.default_name)

        with step('Assert that new card has id and proper name'):
            assert_that(new_card.id, not_none())
            assert_that(new_card.name, equal_to(Parameters.default_name))

    @title('Get exist Card in list')
    def test_get_card_from_list(self, new_list_and_board, new_card, get_cards):
        with step('Create new card'):
            new_card(list=new_list_and_board['list'], name=Parameters.default_name)

        with step('Assert that list contains 1 card'):
            lists_on_board = get_cards(new_list_and_board['list'], )
            assert_that(lists_on_board.count, equal_to(1))
