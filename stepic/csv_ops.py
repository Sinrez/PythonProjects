import csv

# print(csv.list_dialects())

# def reader_sample():
#     with open("Daily_Demand_Forecasting_Orders.csv") as df:
#         reader = csv.reader(df)
#         for row in reader:
#             print(row)


# reader_sample()

# def sniffer():
#     with open("Daily_Demand_Forecasting_Orders.csv") as snif:
#         dialect = csv.Sniffer().sniff(snif.read(1024))
#         snif.seek(0)
#         has_header = csv.Sniffer().has_header(snif.read(1024))
#         snif.seek(0)
#         print("Headers: " + str(has_header))
#         print(dialect.delimiter)
#         print(dialect.escapechar)
#         print(dialect.quotechar)


# sniffer()


# def write_data():
#     with open("Daily_Demand_Forecasting_Orders.csv", mode="w") as csvfile:
#         csv_writer = csv.writer(csvfile)
#         csv_writer.writerow(["Week of the month (first week, second, third, fourth or fifth week", 
#                              "Day of the week (Monday to Friday)",
#                              "Non-urgent order",
#                              "Urgent order",
#                              "Order type A",
#                              "Order type B",
#                              "Order type C",
#                              "Fiscal sector orders",
#                              "Orders from the traffic controller sector",
#                              "Banking orders (1)",
#                              "Banking orders (2)",
#                              "Banking orders (3)",
#                              "Target (Total orders)"])

#         csv_writer.writerow(["1","4","316.307","223.270","61.543","175.586","302.448","0","65556","44914","188411","14793","539.577"])

# write_data()