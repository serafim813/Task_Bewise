import sqlalchemy as sa

metadata = sa.MetaData()

answer = sa.Table(
    'answer',
    metadata,
    sa.Column('id', sa.BigInteger, primary_key=True),
    sa.Column('date', sa.Date, nullable=False),
    sa.Column('answer', sa.String, nullable=False),
    sa.Column('question', sa.String, nullable=False),
)
