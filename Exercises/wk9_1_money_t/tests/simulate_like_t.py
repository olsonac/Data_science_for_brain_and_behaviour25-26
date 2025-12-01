# Array library.
import numpy as np
# Data frames library.
import pandas as pd
# Turn on a setting to use Pandas more safely.
# We will discuss this setting later.
pd.set_option('mode.chained_assignment', 'raise')

# Read the data into a data frame
# One row per respondent.
gss = pd.read_csv('GSS2002.csv')

# Recode the income column.
def recode_income(value):
    import pandas as pd
    import numpy as np

    if pd.isna(value):  # Missing value
        return np.nan
    if value == 'under 1000':
        return 500
    low_str, high_str = value.split('-')
    low, high = int(low_str), int(high_str)
    return np.mean([low, high])

# Get the columns of interest into their own data frame, and recode.
money_death = pd.DataFrame()
money_death['Income'] = gss['Income'].apply(recode_income)
money_death['DeathPenalty'] = gss['DeathPenalty']
# Drop all missing values.
slim_md = money_death.dropna()

income = slim_md['Income']
death = slim_md['DeathPenalty']
favor_income_arr = np.array(income[death == 'Favor'])
oppose_income_arr = np.array(income[death == 'Oppose'])

actual_diff = np.mean(favor_income_arr) - np.mean(oppose_income_arr)

#<- n_favor = ...
n_favor = len(favor_income_arr)
# Concatenate the in-favor and opposed incomes.
pooled = np.append(favor_income_arr, oppose_income_arr)

n_repeats = 1000
fake_stds = np.zeros(n_repeats)
for r in np.arange(n_repeats):
    fake_differences = np.zeros(n_repeats)
    for i in np.arange(n_repeats):
        # Permute the pooled incomes
        shuffled = np.random.permutation(pooled)
        # Make a fake favor sample
        fake_favor = shuffled[:n_favor]
        # Make a fake opposed sample
        fake_oppose = shuffled[n_favor:]
        # Calculate the mean difference for the fake samples
        fake_diff = np.mean(fake_favor) - np.mean(fake_oppose)
        # Put the mean difference into the fake_differences array.
        fake_differences[i] = fake_diff
    fake_stds[r] = np.std(fake_differences)

""" Example:
[2483.83043141 2592.42163534]
[1.74939252 1.82587465]
"""
print(np.quantile(fake_stds, [0.001, 0.999]))
print(np.quantile(actual_diff / fake_stds, [0.001, 0.999]))
