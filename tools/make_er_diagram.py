import os
import sys
from dotenv import load_dotenv
from eralchemy2 import render_er

sys.path.insert(0, os.getcwd())

load_dotenv(os.path.join(os.getcwd(), ".env"))

from database.migration import Migration


class MakeErDiagram:

    def __init__(self) -> None:
        migration = Migration()
        migration.run()
        self.engine = migration.engine

    def generate_er_diagram(self):
        filename = 'er_diagram.png'

        render_er(self.engine.url, filename)


if __name__ == '__main__':
    makeErDiagram = MakeErDiagram()
    makeErDiagram.generate_er_diagram()
