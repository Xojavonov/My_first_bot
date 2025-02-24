from aiogram.fsm.state import StatesGroup,State
class Buttons(StatesGroup):
    films_group=State()
    drams_group=State()
    language=State()
    comedy_film=State()
    action_film=State()
    drama_film=State()
    admin_id=State()
class Admin_State(StatesGroup):
    videos = State()
    picture=State()
    name=State()
    release_year=State()
    rating=State()
    category_id=State()
