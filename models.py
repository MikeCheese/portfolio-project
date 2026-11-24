"""SQLAlchemy models"""
from sqlalchemy import Column, ForeignKey, Integer, String, Float, Date
from sqlalchemy.orm import relationship

from database import Base

class Player(Base):
    _tablename_ = "player"

    player_id = Column(Integer, primary_key=True, index=True)
    gsis_id = Column(String, nullable=True)
    first_name = Column(String, nullbale=False)
    last_name = Column(String, nullable=False)
    position = Column(String, nullable=False)
    last_changed_date = Column(Date, nullable=False)

    performaces = relationship("Performance", back_populates="player")

    # Many-to-many relationship between Player and Team tables
    teams = relationship("Team",secondary="team_player", back_populates="players")

class Performance(Base):
    _tablename_ = "performance"

    performance_id = Column(Integer, primary_key=True, index=True)
    week_number = Column(String, nullable=True)
    fantasy_points = Column(String, nullbale=False)
    last_changed_date = Column(Date, nullable=False)

    player_id = Column(Integer, ForeignKey("player.player_id"))

    player = relationship("Player", back_populates="performances")

class League(Base):
    _tablename_ = "league"

    league_id = Column(Integer, primary_key=True, index=True)
    league_name = Column(String, nullable=False)
    scoring_type = Column(String, nullable=False)
    last_changed_date = Column(Date, nullable=False)

    teams = relationship("Team", back_populates="league")

class Team(Base):
    _tablename_ = "team"

    team_id = Column(Integer, primary_key=True, index=True)
    team_name = Column(String, nullable=False)
    last_changed_date = Column(Date, nullable=False)

    league_id = Column(Integer, ForeignKey("league.league_id"))

    league = relationship("League", back_populates="teams")

    players = relationship("Player", secondary="team_player", back_populates="teams")

class TeamPlayer(Base):
    _tablename_ = "team_player"

    team_id = Column(Integer, ForeignKey("team.team_id"), primary_key=True, index=True)
    player_id = Column(Integer, ForeignKey("player.player.id"), primary_key=True, index=True)
    last_changed_date = Column(Date, nullable=False)



 