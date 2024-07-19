

# Load final version of data package
# Try locate problem with HOME and HOSP
# Getting HOSP data when you select HOME

# Load "HTLN_InvasivePlants_Monitoring.csv" into dataframe

# cd C:\Users\GRowell\HTLN-ProPlants-dashboard-V2\src
# conda activate proplants-dashboard
# jupyter notebook

import numpy as np
import pandas as pd


df = pd.read_csv("HTLN_InvasivePlants_Monitoring.csv")
display(df)

