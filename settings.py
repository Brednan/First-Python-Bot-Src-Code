from cx_Freeze import setup, Executable
setup(
    name="Python.org Data Scraper",
    version="0.1",
    description="This is a Bot that scrapes the search results from the python website, allowing you to store it in a txt file",
    executables=[Executable("gui.py", base="Win32GUI")],
    )
