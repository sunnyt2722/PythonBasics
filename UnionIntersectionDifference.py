India = {"Rohit", "Rahul", "Virat", "Shubhman", "Jaiswal", "Sky", "Bumrah", "Sanju", "Siraj", "Rinku", "Arshdeep", "Shivam"}
Australia = {"Cummins", "Head", "Starc", "Hazlewood", "Marsh", "Warner", "Smith", "Maxwell", "Tim David"}
Africa = {"FAF", "Rabada", "Cotzee", "Markram", "Miller", "Klaseen"}

RCB = {"Virat", "Siraj", "FAF", "Maxwell"}
MI = {"Rohit", "Sky", "Bumrah", "Tim David"}
SRH = {"Cummins", "Head", "Markram", "Klaseen"}

RCB_Indian = India.intersection(RCB)
print(f"Indian players in RCB Team are {RCB_Indian}")

MI_Indian = India.intersection(MI)
print(f"Indian players in MI Team are {MI_Indian}")

RCB_MI_Indian = RCB_Indian.union(MI_Indian)
print(f"Indian players in both RCB and MI are {RCB_MI_Indian}")

Indian_Team_With_No_RCB_MI = India.difference(RCB_MI_Indian)
print(f"Indian players who are not in RCB or MI are {Indian_Team_With_No_RCB_MI}")