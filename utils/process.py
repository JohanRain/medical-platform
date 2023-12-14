from neomodel import config
from neomodel import db
from neomodel.integration.pandas import to_dataframe, to_series
import streamlit as st

config.DATABASE_URL = "bolt://neo4j:developments-cockpits-buzzers@34.234.225.147:7687"


result = db.cypher_query(f"MATCH (a:Person) RETURN keys(a) LIMIT 2")
print(result)
