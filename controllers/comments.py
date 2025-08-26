from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.comment import CommentModel
from models.tea import TeaModel
from serializers.comment import CommentSchema
from typing import List
from database import get_db
# Initialize the router
router = APIRouter()
@router.get("/teas/{tea_id}/comments/", response_model=List[CommentSchema])
def get_comments_for_tea(tea_id: int, db: Session = Depends(get_db)):
    tea = db.query(TeaModel).filter(TeaModel.id == tea_id).first()
    if not tea:
        raise HTTPException(status_code=404, detail="Tea not found")
    return tea.comments
@router.get("/comments/{comment_id}", response_model=CommentSchema)
def get_single_comment(comment_id: int, db: Session = Depends(get_db)):
    comment = db.query(CommentModel).filter(CommentModel.id == comment_id).first()
    if not comment:
        raise HTTPException(status_code=404,detail="Comment not found")
    return comment
@router.post("/teas/{tea_id}/comments/", response_model=CommentSchema)
def create_comment(tea_id: int, comment: CommentSchema, db: Session = Depends(get_db)):
    new_comment = CommentModel(
        content=comment.content,
        tea_id=tea_id
    )
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return new_comment
@router.delete("/comments/{comment_id}")
def delete_comment(comment_id: int, db: Session = Depends(get_db)):
    db_comment = db.query(CommentModel).filter(CommentModel.id == comment_id).first()
    if not db_comment:
        raise HTTPException(status_code=404, detail="Comment not found")
    db.delete(db_comment)  # Remove from database
    db.commit()  # Save changes
    return {"message": f"Comment with ID {comment_id} has been deleted"}