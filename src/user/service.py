from typing import List, Dict

from sqlalchemy import select
from sqlalchemy.future import Engine
import sqlalchemy as sa

from src.database import create_database_url
engine = sa.create_engine(
        create_database_url(),
        future=True
)
from src.tools.jservice_helper import Jservice
from src.database import tables
from src.user.models import (
    StatsAddV12,
)


class UserService:
    def __init__(self, engine: Engine) -> None:
        self._engine = engine

    async def push_answers(self, counts: int) -> None:
        """Check answers and push in databases"""

        def get_all_id_answers() -> Dict:
            query = select(tables.answer.c.id)
            with self._engine.connect() as connection:
                ids = connection.execute(query).fetchall()
            return {t_id[0] for t_id in ids}
        all_id_answers = get_all_id_answers()

        async def check_and_push_answer(counts):
            count = 0
            github = Jservice(self._engine)
            all_stats_rep = await github.get_answer_from_jservice(counts)

            for stats_rep in all_stats_rep:
                if (stats_rep.id not in all_id_answers) and (count < counts):
                    github.push_answer_in_database(stats_rep)
                    id_answer = stats_rep.id
                    count += 1
                else:
                    await check_and_push_answer(1)
            if 'id_answer' not in locals():
                return
            else:
                return id_answer
        id_answer = await check_and_push_answer(counts)
        return id_answer

    def get_last_answer(self, id_answer) -> List[StatsAddV12]:
        """Get last answer in databases"""
        query = select(tables.answer).where(tables.answer.c.id == id_answer)
        with self._engine.connect() as connection:
            answers = connection.execute(query)
        return [StatsAddV12(
                            id=answer['id'],
                            answer=answer['answer'],
                            question=answer['question'],
                            date=answer['date'],
        ) for answer in answers
        ]
