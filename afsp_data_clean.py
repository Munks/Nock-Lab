# Create a new column named accuracy and place data from the choice_prob column in the new accuracy column
# Look at the Reversal column, in all instances where Reversal = 0 go to the accuracy column and change 25 to 0 and 75 to 1
# Look at the Reversal column, in all instances where Reversal = 1 go to the accuracy column and change 25 to 1 and 75 to 0

frame['accuracy']=frame.choice_prob
frame.loc[frame.Reversal==0,'accuracy']=frame[frame.Reversal==0].accuracy.replace({25:0,75:1})
frame.loc[frame.Reversal==1,'accuracy']=frame[frame.Reversal==1].accuracy.replace({25:1,75:0})

# Look at the participants, and for each participant take the mean of their accuracy column

frame.groupby('participant').accuracy.mean()
