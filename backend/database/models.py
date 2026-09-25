from datetime import datetime

from sqlalchemy import (
    Column,
    DateTime,
    Float,
    ForeignKey,
    Integer,
    String,
)

from .connection import Base


class Dataset(Base):
    __tablename__ = "datasets"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String(255), nullable=False)
    rows = Column(Integer, nullable=False)
    columns = Column(Integer, nullable=False)
    uploaded_at = Column(DateTime, default=datetime.utcnow)


class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    dataset_id = Column(Integer, ForeignKey("datasets.id"), nullable=False)

    customer_id = Column(String(100), nullable=False)

    recency = Column(Float)
    history = Column(Float)
    mens = Column(Float)
    womens = Column(Float)
    newbie = Column(Float)

    discount_offered = Column(Integer)
    purchased = Column(Integer)


class AnalysisRun(Base):
    __tablename__ = "analysis_runs"

    id = Column(Integer, primary_key=True, index=True)
    dataset_id = Column(Integer, ForeignKey("datasets.id"), nullable=False)

    ate = Column(Float)
    average_ite = Column(Float)
    positive_pct = Column(Float)
    negative_pct = Column(Float)
    sample_size = Column(Integer)

    created_at = Column(DateTime, default=datetime.utcnow)


class CausalResult(Base):
    __tablename__ = "causal_results"

    id = Column(Integer, primary_key=True, index=True)
    analysis_run_id = Column(
        Integer,
        ForeignKey("analysis_runs.id"),
        nullable=False,
    )

    customer_id = Column(String(100), nullable=False)
    ite = Column(Float, nullable=False)
    effect_category = Column(String(50))