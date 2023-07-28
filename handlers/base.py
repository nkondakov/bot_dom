import decimal
from decimal import Decimal

from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from States.mortgage import MortgageStates


start_router = Router()


@start_router.message(Command("start"))
async def start_bot(message: Message, state: FSMContext) -> None:
    await state.set_state(MortgageStates.loan_amount)
    await message.answer(
        text="Привет! Это бот для оценки возможности взятия ипотечного кредита.\nВведите размер желаемого кредита."
    )


@start_router.message(MortgageStates.loan_amount)
async def loan_size(message: Message, state: FSMContext) -> None:
    try:
        loan_amount = Decimal(message.text)
        await state.update_data(loan_amount=loan_amount)
        await state.set_state(MortgageStates.initial_deposit)
        await message.answer(text="Введите размер первоначального взноса:")
    except decimal.InvalidOperation:
        await message.answer(
            text="К сожалению, я пока умею читать только цифры. Пожалуйста, введите любое число."
        )


@start_router.message(MortgageStates.initial_deposit)
async def initial_deposit(message: Message, state: FSMContext) -> None:
    try:
        deposit_amount = Decimal(message.text)
        data = await state.get_data()
        if deposit_amount > Decimal(0.15) * data["loan_amount"]:
            await state.update_data(initial_deposit=deposit_amount)
            await message.answer(
                "Вы можете подать заявку на ипотеку на сайте:\nhttps://domclick.ru/ipoteka/programs/onlajn-zayavka"
            )
        else:
            await message.answer(
                "К сожалению размер первоначального взноса недостаточен для выдачи такого кредита. "
                "Введите больший первоначальный взнос."
            )
    except decimal.InvalidOperation:
        await message.answer(
            text="К сожалению, я пока умею читать только цифры. Пожалуйста, введите любое число."
        )
