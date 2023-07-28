import decimal

from aiogram.filters.state import StatesGroup, State


class MortgageStates(StatesGroup):
    loan_amount: decimal = State()
    initial_deposit: decimal = State()
