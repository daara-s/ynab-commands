import pytest
import responses
from requests import Session

from tests.data.defaults import DEFAULT_TOKEN
from tests.data.examples import EXAMPLE_TRANSACTION_LIST, EXAMPLE_BUDGET_LIST
from ynab_commands.api import BudgetApi
from ynab_commands.models import TransactionsResponse, BudgetSummaryResponse


@pytest.fixture()
def requests_mock():
    with responses.RequestsMock() as requestsMock:
        yield requestsMock


@pytest.fixture()
def budget_api() -> BudgetApi:
    return BudgetApi(DEFAULT_TOKEN, session=Session())


@pytest.fixture()
def transactions_response_json():
    return EXAMPLE_TRANSACTION_LIST


@pytest.fixture()
def transactions_response():
    return TransactionsResponse(**EXAMPLE_TRANSACTION_LIST["data"])


@pytest.fixture()
def budget_summary_json():
    return EXAMPLE_BUDGET_LIST


@pytest.fixture()
def budget_summary():
    return BudgetSummaryResponse(**EXAMPLE_BUDGET_LIST["data"])
