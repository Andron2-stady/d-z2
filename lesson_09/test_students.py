
import pytest
from sqlalchemy import select
from models import Student, Base
from database import SessionLocal, engine

Base.metadata.create_all(bind=engine)

@pytest.fixture
def db_session():
    """Фикстура для создания и очистки сессии"""
    connection = engine.connect()
    transaction = connection.begin()
    session = SessionLocal(bind=connection)

    yield session

    session.close()
    transaction.rollback()
    connection.close()

def test_add_student(db_session):
    """Тест на добавление"""
    new_student = Student(first_name="Иван", last_name="Петров", group_name="10А")
    db_session.add(new_student)
    db_session.commit()
    db_session.refresh(new_student)

    assert new_student.id is not None

    # Проверка через БД
    stmt = select(Student).where(Student.id == new_student.id)
    result = db_session.execute(stmt).scalar_one_or_none()
    assert result is not None
    assert result.first_name == "Иван"

def test_update_student(db_session):
    """Тест на изменение"""
    student = Student(first_name="Анна", last_name="Сидорова", group_name="11Б")
    db_session.add(student)
    db_session.commit()
    db_session.refresh(student)

    # Изменяем
    student.group_name = "11В"
    db_session.commit()

    stmt = select(Student).where(Student.id == student.id)
    result = db_session.execute(stmt).scalar_one_or_none()
    assert result.group_name == "11В"

def test_delete_student(db_session):
    """Тест на удаление"""
    student = Student(first_name="Антон", last_name="Пименов", group_name="2А")
    db_session.add(student)
    db_session.commit()
    db_session.refresh(student)

    db_session.delete(student)
    db_session.commit()

    stmt = select(Student).where(Student.id == student.id)
    result = db_session.execute(stmt).scalar_one_or_none()
    assert result is None
