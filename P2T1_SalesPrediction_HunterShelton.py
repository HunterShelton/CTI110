#Sales Prediction Tutorial
#9/20/18
#CTI-110 P2T1 -Sales Prediction
#Hunter Shelton

#Get the projected total sales
totalSales=float(input('Enter the projected sales: '))
#Calculate the profit as 23 percent of total sales.
profit = totalSales*0.23
#Display Profit
print ('The profit is $', format(profit, ',.2f'))
