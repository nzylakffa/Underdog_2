import streamlit as st
import pandas as pd
import pandas as pd
import numpy as np
import os

url = 'https://raw.githubusercontent.com/nzylakffa/Underdog_2/main/Underdog%20Optimal%20Drafts.csv'

df = pd.read_csv(url,index_col=0)

st.title("Input Positions Drafted")
st.header("Submit a Max of 9 Rounds!")

### Imput Picks Thus Far ###
picks = st.multiselect(label = "Must be done in order!", options = ["QB", "QB", "QB", "QB", "QB",
                                                              "RB", "RB", "RB", "RB", "RB", "RB", "RB", "RB", "RB",
                                                              "WR", "WR", "WR", "WR", "WR", "WR", "WR", "WR", "WR",
                                                              "TE", "TE", "TE", "TE"])

if len(picks) == 0:
    so_far = df
elif len(picks) == 1:
    so_far = df[df["Round 1"] == picks[0]]
elif len(picks) == 2:
    so_far = df[df["Round 1"] == picks[0]]
    so_far = so_far[so_far["Round 2"] == picks[1]]
elif len(picks) == 3:
    so_far = df[df["Round 1"] == picks[0]]
    so_far = so_far[so_far["Round 2"] == picks[1]]
    so_far = so_far[so_far["Round 3"] == picks[2]]
elif len(picks) == 4:
    so_far = df[df["Round 1"] == picks[0]]
    so_far = so_far[so_far["Round 2"] == picks[1]]
    so_far = so_far[so_far["Round 3"] == picks[2]]
    so_far = so_far[so_far["Round 4"] == picks[3]]
elif len(picks) == 5:
    so_far = df[df["Round 1"] == picks[0]]
    so_far = so_far[so_far["Round 2"] == picks[1]]
    so_far = so_far[so_far["Round 3"] == picks[2]]
    so_far = so_far[so_far["Round 4"] == picks[3]]
    so_far = so_far[so_far["Round 5"] == picks[4]]
elif len(picks) == 6:
    so_far = df[df["Round 1"] == picks[0]]
    so_far = so_far[so_far["Round 2"] == picks[1]]
    so_far = so_far[so_far["Round 3"] == picks[2]]
    so_far = so_far[so_far["Round 4"] == picks[3]]
    so_far = so_far[so_far["Round 5"] == picks[4]]
    so_far = so_far[so_far["Round 6"] == picks[5]]
elif len(picks) == 7:
    so_far = df[df["Round 1"] == picks[0]]
    so_far = so_far[so_far["Round 2"] == picks[1]]
    so_far = so_far[so_far["Round 3"] == picks[2]]
    so_far = so_far[so_far["Round 4"] == picks[3]]
    so_far = so_far[so_far["Round 5"] == picks[4]]
    so_far = so_far[so_far["Round 6"] == picks[5]]
    so_far = so_far[so_far["Round 7"] == picks[6]]
elif len(picks) == 8:
    so_far = df[df["Round 1"] == picks[0]]
    so_far = so_far[so_far["Round 2"] == picks[1]]
    so_far = so_far[so_far["Round 3"] == picks[2]]
    so_far = so_far[so_far["Round 4"] == picks[3]]
    so_far = so_far[so_far["Round 5"] == picks[4]]
    so_far = so_far[so_far["Round 6"] == picks[5]]
    so_far = so_far[so_far["Round 7"] == picks[6]]
    so_far = so_far[so_far["Round 8"] == picks[7]]
elif len(picks) == 9:
    so_far = df[df["Round 1"] == picks[0]]
    so_far = so_far[so_far["Round 2"] == picks[1]]
    so_far = so_far[so_far["Round 3"] == picks[2]]
    so_far = so_far[so_far["Round 4"] == picks[3]]
    so_far = so_far[so_far["Round 5"] == picks[4]]
    so_far = so_far[so_far["Round 6"] == picks[5]]
    so_far = so_far[so_far["Round 7"] == picks[6]]
    so_far = so_far[so_far["Round 8"] == picks[7]]
    so_far = so_far[so_far["Round 9"] == picks[8]]
    
### Suggest Next Pick Position ###
if len(picks) == 0:
    options = so_far.groupby("Round 1").agg({'Average Points': 'mean'})
    rod_qb = so_far["QBs in Final 9"].mean()
    rod_rb = so_far["RBs in Final 9"].mean()
    rod_wr = so_far["WRs in Final 9"].mean()
    rod_te = so_far["TEs in Final 9"].mean()
elif len(picks) == 1:
    options = so_far.groupby("Round 2").agg({'Average Points': 'mean'})
    rod_qb = so_far["QBs in Final 9"].mean()
    rod_rb = so_far["RBs in Final 9"].mean()
    rod_wr = so_far["WRs in Final 9"].mean()
    rod_te = so_far["TEs in Final 9"].mean()
elif len(picks) == 2:
    options = so_far.groupby("Round 3").agg({'Average Points': 'mean'})
    rod_qb = so_far["QBs in Final 9"].mean()
    rod_rb = so_far["RBs in Final 9"].mean()
    rod_wr = so_far["WRs in Final 9"].mean()
    rod_te = so_far["TEs in Final 9"].mean()
elif len(picks) == 3:
    options = so_far.groupby("Round 4").agg({'Average Points': 'mean'})
    rod_qb = so_far["QBs in Final 9"].mean()
    rod_rb = so_far["RBs in Final 9"].mean()
    rod_wr = so_far["WRs in Final 9"].mean()
    rod_te = so_far["TEs in Final 9"].mean()
elif len(picks) == 4:
    options = so_far.groupby("Round 5").agg({'Average Points': 'mean'})
    rod_qb = so_far["QBs in Final 9"].mean()
    rod_rb = so_far["RBs in Final 9"].mean()
    rod_wr = so_far["WRs in Final 9"].mean()
    rod_te = so_far["TEs in Final 9"].mean()
elif len(picks) == 5:
    options = so_far.groupby("Round 6").agg({'Average Points': 'mean'})
    rod_qb = so_far["QBs in Final 9"].mean()
    rod_rb = so_far["RBs in Final 9"].mean()
    rod_wr = so_far["WRs in Final 9"].mean()
    rod_te = so_far["TEs in Final 9"].mean()
elif len(picks) == 6:
    options = so_far.groupby("Round 7").agg({'Average Points': 'mean'})
    rod_qb = so_far["QBs in Final 9"].mean()
    rod_rb = so_far["RBs in Final 9"].mean()
    rod_wr = so_far["WRs in Final 9"].mean()
    rod_te = so_far["TEs in Final 9"].mean()
elif len(picks) == 7:
    options = so_far.groupby("Round 8").agg({'Average Points': 'mean'})
    rod_qb = so_far["QBs in Final 9"].mean()
    rod_rb = so_far["RBs in Final 9"].mean()
    rod_wr = so_far["WRs in Final 9"].mean()
    rod_te = so_far["TEs in Final 9"].mean()
elif len(picks) == 8:
    options = so_far.groupby("Round 9").agg({'Average Points': 'mean'})
    rod_qb = so_far["QBs in Final 9"].mean()
    rod_rb = so_far["RBs in Final 9"].mean()
    rod_wr = so_far["WRs in Final 9"].mean()
    rod_te = so_far["TEs in Final 9"].mean()
elif len(picks) == 9:
    options = so_far.groupby("Round 9").agg({'Average Points': 'mean'})
    rod_qb = so_far["QBs in Final 9"].mean()
    rod_rb = so_far["RBs in Final 9"].mean()
    rod_wr = so_far["WRs in Final 9"].mean()
    rod_te = so_far["TEs in Final 9"].mean()

n = len(options)    
options = options['Average Points'].round(0)
options = options.sort_values(ascending = False)
final_9_dfs = [rod_qb, rod_rb, rod_wr, rod_te]
final_9 = pd.DataFrame([final_9_dfs], columns = ["QBs", "RBs", "WRs", "TEs"])

st.write("* The below table displays what position you should draft next.")
st.write("* If the table is empty then no drafts for that build have been simulated.")
st.write("You can submit new builds to be run here: ")
st.write("https://docs.google.com/forms/d/e/1FAIpQLScU-QkFbC1ld95W8uiLUMNHg3liCPsnOGzTxpJsN1f0_4VPAg/viewform")
st.write("Total Sample Size: ", len(so_far))

st.dataframe(data = options)

st.header("Suggested Finish in Final 9 Rounds")
st.write("* This table shows the suggested makup of the final 9 rounds")
st.write("* This becomes more accurate each round you complete")
st.write("* Will show as <NA> if you submit a build that hasn't been run yet")
st.dataframe(final_9)