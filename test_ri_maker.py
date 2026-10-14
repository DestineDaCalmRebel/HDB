from pathlib import Path
import pandas as pd

def Recommended_Intakes(record):

    base = Path(f'Nutrients/{record}')
    folder = Path(f'{base}/recommended_intake')
    
    target_id = None
    symbol = None

    body_type = ['Male', 'Female', 'Pregnant', 'Lactate']
    age_range = [(0,0.5),(0.51,0.99),(1,3),(4,8),(9,13),(14,18),(19,30),(31,50),(51,70),(71,"+")]

    create 
    #with open (base / f'mi{symbol}db.exl', 'w') as file:


    with open(base / f'id_{record}.txt', 'r') as r:
            #Grab the folder id and symbol from the main file
            target_id = r.readlines()[0].strip().lower()
            symbol = r.readlines()[2].strip().lower()

    
    

    for file in folder.glob("*.txt"):
            lines = file.read_text().splitlines()
            #Matchs the folder id with the connection id of the current file, if they match, the program continues
            file_id = lines[1].strip()

            if file_id == target_id:
                   #organizes the data for easy access and manipulation
                   age_min=lines[2],age_max=lines[3],sex=lines[4],
                   is_pregnant=lines[5],is_lactate=lines[6],
                   size=lines[7],unit=lines[8],sources=lines[9:]
                            

