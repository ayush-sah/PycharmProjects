import pandas as pd
import matplotlib.pyplot as plt

data = [['S01', 'M', 24, 93, 'BCA'],
        ['S02', 'F', 20, 74, 'BSC IT'],
        ['S03', 'F', 27, 75, 'BCA'],
        ['S04', 'M', 20, 99, 'BSC CS'],
        ['S05', 'F', 24, 77, 'BSC CS'],
        ['S06', 'M', 26, 91, 'BCA'],
        ['S07', 'M', 22, 73, 'BSC CS'],
        ['S08', 'F', 26, 80, 'BSC IT'],
        ['S09', 'M', 22, 63, 'BSC IT'],
        ['S10', 'M', 26, 53, 'BCA']]

df = pd.DataFrame(data, columns=['STUID', 'Gender', 'Age', 'Marks', 'GRAD'])

# Histogram
df.hist()
plt.suptitle("Histogram")
plt.show()

# Column Chart
df.plot.bar()
plt.bar(df['Age'], df['Marks'])
plt.xlabel("Age")
plt.ylabel("Marks")
plt.suptitle("Column Chart")
plt.show()

# Box Plot Chart
df.plot.box()
plt.boxplot(df['Age'])
plt.suptitle("Box Plot Chart")
plt.show()

# Pie Chart
plt.pie(df['Age'], labels={"A", "B", "C", "D", "E", "F", "G", "H", "I", "J"}, autopct='% 1.1f %%', shadow=True)
plt.suptitle("Pie Chart")
plt.show()

# Scatter plot
plt.scatter(df['Marks'], df['Age'])
plt.suptitle("Scatter Plot Chart")
plt.show()
