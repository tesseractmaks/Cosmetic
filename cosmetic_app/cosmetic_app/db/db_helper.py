from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, async_scoped_session, AsyncSession
from asyncio import current_task
from cosmetic_app.core import settings


class DatabaseHelper:
    def __init__(self, url: str, echo: bool):
        self.engine = create_async_engine(
            url=url,
            echo=echo
        )

        self.session_factory = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False,
        )

    def get_scopped_session(self):
        session = async_scoped_session(
            session_factory=self.session_factory,
            scopefunc=current_task,
        )
        return session

    async def scopped_session_dependency(self) -> AsyncSession:
        session = self.get_scopped_session()
        yield session
        await session.remove()


db_helper = DatabaseHelper(
    settings.db_url,
    settings.db_echo,
)