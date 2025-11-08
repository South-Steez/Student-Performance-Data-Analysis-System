import csv
import random
 
def generate_data():
    # Generate random data for the example
    data = [["Student number", "Student age", "Average hours spent studying", "Student mark achieved", "Time taken on examination (minutes)"]]
 
    for student_number in range(1, 151):
        student_age = random.choice([random.randint(18, 25), random.randint(25, 35), random.randint(35, 45), random.randint(45, 60)])
        hours_studying = random.choice([1, 2, 3, 4, 5])
        mark_achieved = random.randint(0, 130)
        time_taken = random.randint(90, 180)  # Assuming 90 to 180 minutes for time taken
 
        data.append([student_number, student_age, hours_studying, mark_achieved, time_taken])
 
    return data
 
def save_csv(dataset, filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(dataset)
 
# Generate and save Dataset 1
dataset1 = generate_data()
save_csv(dataset1, 'dataset1.csv')
 
# Generate and save Dataset 2
dataset2 = generate_data()
save_csv(dataset2, 'dataset2.csv')

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load datasets
dataset1 = pd.read_csv('dataset1.csv')
dataset2 = pd.read_csv('dataset2.csv')

# Data cleaning: Remove rows where Student mark is zero
dataset1 = dataset1[dataset1['Student mark achieved'] != 0]
dataset2 = dataset2[dataset2['Student mark achieved'] != 0]

# Frequency table for Average hours spent on campus
average_hours_freq1 = dataset1['Average hours spent studying'].value_counts().sort_index()
average_hours_freq2 = dataset2['Average hours spent studying'].value_counts().sort_index()

# Frequency table for Student age
student_age_freq1 = dataset1['Student age'].value_counts().sort_index()
student_age_freq2 = dataset2['Student age'].value_counts().sort_index()

# Frequency table for Student mark
student_mark_freq1 = dataset1['Student mark achieved'].value_counts().sort_index()
student_mark_freq2 = dataset2['Student mark achieved'].value_counts().sort_index()

# Set up subplots
fig, axes = plt.subplots(3, 2, figsize=(15, 12))

# Plot bar charts for Average hours spent on campus
sns.barplot(x=average_hours_freq1.index, y=average_hours_freq1.values, ax=axes[0, 0])
axes[0, 0].set_title('Average hours spent on campus - Dataset 1')

sns.barplot(x=average_hours_freq2.index, y=average_hours_freq2.values, ax=axes[0, 1])
axes[0, 1].set_title('Average hours spent on campus - Dataset 2')

# Plot bar charts for Student age
sns.barplot(x=student_age_freq1.index, y=student_age_freq1.values, ax=axes[1, 0])
axes[1, 0].set_title('Student age - Dataset 1')

sns.barplot(x=student_age_freq2.index, y=student_age_freq2.values, ax=axes[1, 1])
axes[1, 1].set_title('Student age - Dataset 2')

# Plot bar charts for Student mark
sns.barplot(x=student_mark_freq1.index, y=student_mark_freq1.values, ax=axes[2, 0])
axes[2, 0].set_title('Student mark - Dataset 1')

sns.barplot(x=student_mark_freq2.index, y=student_mark_freq2.values, ax=axes[2, 1])
axes[2, 1].set_title('Student mark - Dataset 2')

# Adjust layout
plt.tight_layout()
plt.show()



import pandas as pd
import matplotlib.pyplot as plt

# Load datasets
dataset1 = pd.read_csv('dataset1.csv')
dataset2 = pd.read_csv('dataset2.csv')

# Data cleaning: Remove rows where Student mark is zero
dataset1 = dataset1[dataset1['Student mark achieved'] != 0]
dataset2 = dataset2[dataset2['Student mark achieved'] != 0]

# Initialize empty dictionaries for frequency tables
average_hours_freq1 = {}
average_hours_freq2 = {}
student_age_freq1 = {}
student_age_freq2 = {}
student_mark_freq1 = {}
student_mark_freq2 = {}

# Generate Frequency Tables using dictionaries
for age_group in ['18-25', '25-35', '35-45', '45-60']:
    student_age_freq1[age_group] = dataset1[dataset1['Student age'].between(*map(int, age_group.split('-')))]['Student age'].count()
    student_age_freq2[age_group] = dataset2[dataset2['Student age'].between(*map(int, age_group.split('-')))]['Student age'].count()

for hours in range(1, 6):
    average_hours_freq1[hours] = dataset1[dataset1['Average hours spent studying'] == hours]['Average hours spent studying'].count()
    average_hours_freq2[hours] = dataset2[dataset2['Average hours spent studying'] == hours]['Average hours spent studying'].count()

for mark in range(1, 131):
    student_mark_freq1[mark] = dataset1[dataset1['Student mark achieved'] == mark]['Student mark achieved'].count()
    student_mark_freq2[mark] = dataset2[dataset2['Student mark achieved'] == mark]['Student mark achieved'].count()

# Create a bar chart for ages and numbers of students
plt.figure(figsize=(10, 6))
plt.bar(student_age_freq1.keys(), student_age_freq1.values(), label='Dataset 1')
plt.bar(student_age_freq2.keys(), student_age_freq2.values(), label='Dataset 2', alpha=0.7)
plt.xlabel('Student Age Groups')
plt.ylabel('Number of Students')
plt.title('Ages and Numbers of Students')
plt.legend()
plt.show()

# Create a line graph for correlation between higher marks and more time spent on campus
plt.figure(figsize=(10, 6))
plt.plot(dataset1['Student mark achieved'], dataset1['Time taken on examination (minutes)'], 'o', label='Dataset 1')
plt.plot(dataset2['Student mark achieved'], dataset2['Time taken on examination (minutes)'], 'o', label='Dataset 2')
plt.xlabel('Student Mark Achieved')
plt.ylabel('Time Taken on Examination (minutes)')
plt.title('Correlation between Marks and Time Spent on Campus')
plt.legend()
plt.show()

# Create a scatter chart for each student’s mark and the time taken on the examination
plt.figure(figsize=(10, 6))
plt.scatter(dataset1['Student mark achieved'], dataset1['Time taken on examination (minutes)'], label='Dataset 1')
plt.scatter(dataset2['Student mark achieved'], dataset2['Time taken on examination (minutes)'], label='Dataset 2')
plt.xlabel('Student Mark Achieved')
plt.ylabel('Time Taken on Examination (minutes)')
plt.title('Scatter Chart: Student Mark vs Time Taken on Examination')
plt.legend()
plt.show()

# Create a scatter chart for the relationship between time spent on campus and the student’s age
plt.figure(figsize=(10, 6))
plt.scatter(dataset1['Average hours spent studying'], dataset1['Student age'], label='Dataset 1')
plt.scatter(dataset2['Average hours spent studying'], dataset2['Student age'], label='Dataset 2')
plt.xlabel('Average Hours Spent Studying on Campus')
plt.ylabel('Student Age')
plt.title('Scatter Chart: Time Spent on Campus vs Student Age')
plt.legend()
plt.show()




