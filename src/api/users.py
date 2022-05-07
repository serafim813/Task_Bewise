from fastapi import APIRouter, status, Depends

from src.api.protocols import UserServiceProtocol

from src.user.models import StatsAddV1

router = APIRouter(
    tags=['Users']
)

@router.post(
    path='/v1/user',
    status_code=status.HTTP_201_CREATED,
    summary='Добавить вопросы',
    description='Добавляет заданное количество вопросов',
)
async def add_answer(
    num: StatsAddV1,
    user_service: UserServiceProtocol = Depends()
):
    id_answer = await user_service.push_answers(num.questions_num)

    return user_service.get_last_answer(id_answer)


