from Experiment import Experiment
from datetime import datetime

print("Start")
a = datetime.now()
exp = Experiment("Exp1", "trial_data.json", ["EyeTracker", "EEG"])

# exp.analyse(standardise_flag = True)
exp.visualizeData()

b = datetime.now()
print("End")
print("Total time taken: ", (b-a).seconds)