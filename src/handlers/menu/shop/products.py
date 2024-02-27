from aiogram import Router, F, types
from aiogram.filters import StateFilter, Command
from aiogram.fsm.context import FSMContext
from aiogram.utils.text_decorations import html_decoration as _t

from src.figaro.api import FigaroAPI
from src.data.texts import Texts
from src.figaro.exceptions import DataIsEmpty, InvalidRequest

products_router = Router()


@products_router.message(F.text == "↘️ Получить продукт")
@products_router.message(Command("get_product"))
async def cmd_get_product(message: types.Message, state: FSMContext):
    await message.answer('<b>#️⃣ Введите номер продукта</b>'
                         '\n\n<i>Например: 13 или 000000013</i>')
    await state.set_state('get_product-get_product_code')


@products_router.message(StateFilter("get_product-get_product_code"))
async def state_get_product_code(message: types.Message, state: FSMContext):
    try:
        async with FigaroAPI() as fg:
            product = await fg.get_product(message.text.rjust(9, "0"))
    except DataIsEmpty:
        return await message.answer(_t.bold('⚠️ Продукт не найден'))
    finally:
        await state.clear()

    await message.answer(Texts.product_info.format(
        product["code"], product["name"], product["weight"], product["size"],
        product["price"], product["costPrice"], product["remainder"]))


@products_router.message(F.text == "📝 Создать продукт")
@products_router.message(Command("create_product"))
async def cmd_get_product(message: types.Message, state: FSMContext):
    await message.answer('#️⃣ Введите наименование продукта')
    await state.set_state('create_product-get_product_name')


@products_router.message(StateFilter("create_product-get_product_name"))
async def state_get_product_name(message: types.Message, state: FSMContext):
    await state.update_data(product_name=message.text)
    await message.answer('⚖️ Введите вес продукта')
    await state.set_state('create_product-get_product_weight')


@products_router.message(StateFilter("create_product-get_product_weight"))
async def state_get_product_weight(message: types.Message, state: FSMContext):
    await state.update_data(product_weight=message.text)
    await message.answer('📐 Введите размер продукта')
    await state.set_state('create_product-get_product_size')


@products_router.message(StateFilter("create_product-get_product_size"))
async def state_get_product_size(message: types.Message, state: FSMContext):
    await state.update_data(product_size=message.text)
    product_data = await state.get_data()
    product_name = product_data.get('product_name')
    product_weight = product_data.get('product_weight')
    product_size = product_data.get('product_size')

    try:
        async with FigaroAPI() as fg:
            await fg.create_product(product_name, product_weight, product_size)
    except InvalidRequest:
        return await message.answer(_t.bold('⚠️ Не удалось создать продукт'))
    finally:
        await state.clear()

    await message.answer(_t.bold("✅ Продукт успешно создан"))

