from parser import course
from db_worker import db_create, add_data, print_all_entries, return_all_entries
from chart_gen import create_comparison_chart

db_create()
add_data()
print_all_entries()

create_comparison_chart(return_all_entries())

