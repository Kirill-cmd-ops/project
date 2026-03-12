from sqlalchemy import select

from db import session_factory
from models import Submission


def get_all_submissions_service():
    with session_factory() as session:
        result = session.scalars(select(Submission)).all()
        return [{"id": obj.id, "data": obj.data} for obj in result]


def create_submission_service(data: dict):
    with session_factory() as session:
        submission = Submission(data=data)
        session.add(submission)
        session.commit()
