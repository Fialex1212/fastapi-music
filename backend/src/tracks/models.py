from sqlalchemy import Column, String, LargeBinary
from ..database import Base
import uuid

class Track(Base):
    __tablename__ = "tracks"

    id = Column(String, primary_key=True, nullable=False, default=lambda: str(uuid.uuid4()), unique=True, index=True)
    title = Column(String, nullable=False)
    artist = Column(String, nullable=False)
    data_file = Column(LargeBinary, nullable=False)