#!/usr/bin/env python3
"""DBStorage class for the Hospital prescription management system"""

import os
from sqlalchemy.orm import sessionmaker
from app.models.audit_log import AuditLog
from app.models.prescription import Prescription, Med
from app.models.user import Users
from app.models.patient import Patients
from app.models.doctor import Doctors
from app.models.otp import OTP
from app.models.pharmacist import Pharmacists
from app.models.dispensation import Dispensation
from app.models.user import OnBoarders

import pymysql


class DBStorage:
    """DBStorage class for the Hospital prescription management system"""

    def __init__(self):
        """Initializes the DBStorage instance"""
        from sqlalchemy import create_engine
        from app.models.base_model import Base

        self.__engine = create_engine(
            "mysql+pymysql://{}:{}@{}/{}".format(
                os.getenv("HPMS_MYSQL_USER"),
                os.getenv("HPMS_MYSQL_PWD"),
                os.getenv("HPMS_MYSQL_HOST"),
                os.getenv("HPMS_MYSQL_DB"),
            ),
            pool_pre_ping=True,
        )
        if os.getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on the current database session all
        objects of the given class"""
        classes = [
            Patients,
            Prescription,
            Pharmacists,
            OTP,
            Dispensation,
            AuditLog,
            Med,
            Users,
            Doctors,
            OnBoarders,
        ]
        objects = []
        if cls:
            if cls in classes:
                for obj in self.__session.query(cls).all():
                    objects.append((obj))
        else:
            for cls in classes:
                for obj in self.__session.query(cls).all():
                    objects.append((obj))
        return objects

    def new(self, obj):
        """Add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session obj if not None"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database and
        the current database session"""
        from sqlalchemy.orm import scoped_session
        from app.models.base_model import Base

        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Close the current session"""
        self.__session.close()

    def get(self, cls, id):
        """get an object from the database"""
        if cls is not None and id is not None:
            obj = self.__session.query(cls).get(id)
            return obj
        return None

    def update(self, obj, data):
        if obj is None or data is None:
            return None
        for key, value in data.items():
            if hasattr(obj, key):
                setattr(obj, key, value)
        self.save()
        return obj

    def get_by_email(self, cls, email):
        """get an object from the database"""
        if cls is not None and email is not None:
            obj = self.__session.query(cls).filter_by(email=email).first()
            return obj
        return None

    def get_by_code(self, cls, code):
        """get an object from the database"""
        if cls is not None and code is not None:
            obj = self.__session.query(cls).filter_by(otp_code=code).first()
            return obj
        return None
