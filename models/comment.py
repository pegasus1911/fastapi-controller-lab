from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import BaseModel

#  TeaModel extends SQLAlchemy's Base class.
#  Extending Base lets SQLAlchemy 'know' about our model, so it can use it.

class CommentModel(BaseModel):

    # This will be used directly to make a
    # TABLE in Postgresql
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String, nullable=False)
    # ForeignKey establishes a connection to the teas table
    tea_id = Column(Integer, ForeignKey('teas.id'), nullable=False)
    tea = relationship("TeaModel", back_populates="comments")  # Defines the relationship to the TeaModel
    



