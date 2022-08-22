# -*- coding: utf-8 -*-
# Data preparation for the hello_world example
from __future__ import print_function

from sqlalchemy import create_engine
from cubes.tutorial.sql import create_table_from_csv

# 1. Prepare SQL data in memory

FACT_TABLE = "irbd_fotografie"

print("preparing data...")

engine = create_engine('sqlite:///data.sqlite')

create_table_from_csv(engine,
                      "export_data_fotografia.csv",
                      table_name=FACT_TABLE,
                      fields=[
                            ("id_fotografia", "integer"),
                            ("fotografia", "string"),
                            ("id_fotografo", "integer"),
                            ("fotografo", "string"),
                            ("nazionalita", "string"),
                            ("id_concorso", "integer"),
                            ("concorso", "string"),
                            ("digitale", "integer"),
                            ("year", "integer"),
                            ("voto", "integer")],
                      create_id=True
                  )

print("done. file data.sqlite created")
