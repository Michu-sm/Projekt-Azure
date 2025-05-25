from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Team(Base):
    __tablename__ = "teams"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    rank = Column(Integer)
    win_rate = Column(Float)

class Player(Base):
    __tablename__ = "players"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    team_id = Column(Integer, ForeignKey("teams.id"))
    rating = Column(Float)

class MatchStat(Base):
    __tablename__ = "match_stats"
    id = Column(Integer, primary_key=True)
    player_id = Column(Integer, ForeignKey("players.id"))
    vs_team_id = Column(Integer, ForeignKey("teams.id"))
    performance_score = Column(Float)
