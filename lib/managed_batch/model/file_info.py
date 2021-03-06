# Copyright 2017 The Jackson Laboratory
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from sqlalchemy import *
from base import Base
import logging
from session import Session


class FileInfo(Base):
    __tablename__ = 'file_info'

    id = Column(Integer, primary_key=True, autoincrement=True)
    schema_version = Column(Integer, nullable=False)
    started = Column(Boolean, nullable=False)
    CURRENT_SCHEMA_VERSION = 1

    def __init__(self):
        """
        Write one row to the file_info table, with the schema version and
        the "started" status False.
        """
        #
        # Have we been initialized before? If so, schema_version should be
        # FileInfo.CURRENT_SCHEMA_VERSION.  If not, we need to initialize.
        #
        logging.debug("In FileInfo constructor. schema_version is: {}.\n"
                      "\t started is {}.".format(
            self.schema_version, self.started
        ))
        if self.schema_version is None:
            logging.debug("Initializing FileInfo table")
            self.schema_version = FileInfo.CURRENT_SCHEMA_VERSION
            self.started = False
            Session.add(self)
            Session.commit()

    def __str__(self):
        return "schema_version: {}  started: {}".format(self.schema_version,
                                                        self.started)

    @staticmethod
    def set_started(b):
        inf = Session.query(FileInfo).one()
        inf.started = b
        Session.commit()
        logging.debug("FileInfo: {}".format(inf))
        logging.debug("File is now marked as submitted.")

    @staticmethod
    def is_started():
        inf = Session.query(FileInfo).one()
        return inf.started

    @staticmethod
    def is_current_schema():
        inf = Session.query(FileInfo).one()
        return inf.schema_version == FileInfo.CURRENT_SCHEMA_VERSION
