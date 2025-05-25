from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Team, Player, MatchStat

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/best_team")
def best_team(db: Session = Depends(get_db)):
    return db.query(Team).order_by(Team.win_rate.desc()).first()

@app.get("/best_player")
def best_player(db: Session = Depends(get_db)):
    return db.query(Player).order_by(Player.rating.desc()).first()

@app.get("/best_player_vs/{team_id}")
def best_player_vs(team_id: int, db: Session = Depends(get_db)):
    return db.query(MatchStat).filter(MatchStat.vs_team_id == team_id)        .order_by(MatchStat.performance_score.desc()).first()
