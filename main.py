# Oura Ring Data: 2022-08-21/2022-10-21  -  61 day period

import math
import csv
from csv import writer

# file_path - Oura Data, file_path_2 - Oura_Analysis File
file_path, file_path_2 = "/home/christopher/PycharmProjects/Oura_Analysis/oura_2022-08-21_2022-10-21_trends.csv", "/home/christopher/PycharmProjects/Oura_Analysis/oura_analysis.csv"


# extract headers & values from Oura Data in lists
rows = []
with open(file_path, 'r') as file:
  csvreader = csv.reader(file)
  header = next(csvreader)
  for row in csvreader:
    rows.append(row)

# metrics from oura that you want to compare
metrics = "Total Sleep Duration Total Bedtime Awake Time REM Sleep Duration Light Sleep Duration Deep Sleep Duration Sleep Efficiency (Total Sleep Duration/Total Bedtime) Sleep Latency Sleep Timing Average Resting Heart Rate Lowest Resting Heart Rate Average HRV Temperature Deviation (°C) Temperature Trend Deviation Respiratory Rate Activity Burn Total Burn Steps Equivalent Walking Distance Inactive Time Rest Time Low Activity Time Medium Activity Time High Activity Time Non-wear Time Average MET Long Periods of Inactivity Previous Night Score Previous Day Activity Score Activity Score Sleep Score Total Sleep Score"

# user input for which category you want to use data
# match all headers with each other
used_head = []
for head1 in header:
  used_head.append(head1)
  for head2 in header:
    ui1, ui2 = head1, head2

    # don't have duplicates fE (x, x, r = ...)
    if ui1 == ui2 or ui2 in used_head or ui1 and ui2 not in metrics:
      continue

    else:
      try:
        # find index for values in rows by header
        def find_indx(ui, titles):
          sum = 0
          for title in titles:
            if title == ui:
              #print(sum)
              break
            else:
              sum += 1
          return sum
        indx_1, indx_2 = find_indx(ui1, header), find_indx(ui2, header)
        
        # list all data points under head
        def all_data(t):
          data = []
          for i in range(len(rows)):
            x = rows[i][t]
            data.append(x)
          return data
        all_data_1, all_data_2 = all_data(indx_1), all_data(indx_2)

        # removing rows with empty strings and "None" Values, and storing rest of the items
        def rem_emptystr(data):
          i = 0
          fal_val = []
          for item in data:
            if item == "" or item == "None":
              fal_val.append(i)
              i += 1

            else:
              i+= 1

          return fal_val
      # returns list with indx of removed rows
        fal_val_1, fal_val_2 = rem_emptystr(all_data_1), rem_emptystr(all_data_2)
        
        # list with all items that have to be removed, cleaned for duplicates
        all_fal_val = fal_val_1
        for val in fal_val_2:
          if val not in fal_val_1:
            all_fal_val.append(val)
          else:
            continue
        
        # cleaned up data, removed for "" and "None"
        def clean_data(all_data):
          clean_data = []
          i = 0
          for item in all_data:
            if i not in all_fal_val:
              clean_data.append(item)
              i += 1
            else:
              i += 1
          return clean_data
        clean_data_1, clean_data_2 = clean_data(all_data_1), clean_data(all_data_2)
        

        # math functions
        # sum data in list
        def var_sum(clean_data):
          sum = 0
          for item in clean_data:
            sum += float(item)
          return sum
        
        # sum of ( xi * yi)
        def x_y_sum(x, y):
          x_y = []
          for i in range(len(x)):
            z = float(x[i]) * float(y[i])
            x_y.append(z)
          s = 0
          for item in x_y:
            s += float(item)
          return s
        
        # sum of (k^2)
        def sum_sq(clean_data):
          sum = 0
          for item in clean_data:
            sum = sum + float(item) * float(item)
          return(sum)

        # calculate values
        x_sum, y_sum = var_sum(clean_data_1), var_sum(clean_data_2)
        n = len(clean_data_1)
        x_sum_sq, y_sum_sq = sum_sq(clean_data_1), sum_sq(clean_data_2)
        xy_sum = x_y_sum(clean_data_1, clean_data_2)

        # calculate r
        a = (n * xy_sum - (x_sum) * (y_sum)) 
        b = (math.sqrt(n * x_sum_sq - (x_sum) ** 2) * math.sqrt(n * y_sum_sq - (y_sum) ** 2))
        r = a/b

        # Output (x, y, r)
        out = head1, head2, r

        print(out)

        # append out to file_path_2
        with open(file_path_2, 'a') as f_object:
          writer_object = writer(f_object)
          writer_object.writerow(out)
          f_object.close()
          
      # because not all data is in calc format (fE date)
      except ValueError:
        print("")


