import os
import platform
import subprocess
from pathlib import Path



def Header(record):

    #Uses id
    
    with open(f'Nutrients/{record}/id_{record}.txt', "r") as f:
        record = f.read().strip()

    id,name,abbrv,typ,status = record.splitlines()
    print(f"{name}\n{abbrv}\n{typ}\n{status}")


def Functions(record):
    base = Path(f'Nutrients/{record}')
    folder = base / 'nutrient_functions'

    # Read the reference id, outside the loop
    with open(base / f'id_{record}.txt', 'r') as r:
        target_id = r.readlines()[0].strip()

    descriptions = []
    sources = []

    for file in folder.glob("*.txt"):
        lines = file.read_text().splitlines()
        
        file_id = lines[1].strip()
        description = lines[2].strip()
        source_lines = lines[3:]

        if file_id == target_id:
            descriptions.append(description)
            sources.append(source_lines)

            print("\n",descriptions,"\n",sources)


                        

def Decficiency(record):
    base = Path(f'Nutrients/{record}')
    folder = base / 'nutrient_decficiencies'

    with open(base / f'id_{record}.txt', 'r') as r:
        target_id = r.readlines()[0].strip()

    descriptions = []
    sources = []

    for file in folder.glob("*.txt"):
        lines = file.read_text().splitlines()
        
        file_id = lines[1].strip()
        description = lines[2].strip()
        source_lines = lines[3:]

        if file_id == target_id:
            descriptions.append(description)
            sources.append(source_lines)

            print("\n",descriptions,"\n",sources)


def Overdose(record):
    base = Path(f'Nutrients/{record}')
    folder = base / 'nutrient_overdose'

    with open(base / f'id_{record}.txt', 'r') as r:
        target_id = r.readlines()[0].strip()

    descriptions = []
    sources = []

    for file in folder.glob("*.txt"):
        lines = file.read_text().splitlines()
        
        file_id = lines[1].strip()
        description = lines[2].strip()
        source_lines = lines[3:]

        if file_id == target_id:
            descriptions.append(description)
            sources.append(source_lines)

            print("\n",descriptions,"\n",sources)

def Recommended_Intakes():
    print()


def page_maker(record):
    Header(record)
    Functions(record)
    Decficiency(record)
    Overdose(record)

    
