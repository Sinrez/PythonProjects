import calendar

cal = calendar.month(2023, 1)

print(cal)

print(type(cal))

###################

cal = calendar.month(2023, 1, w=5, l=5)

print(cal)

#############

cal_mnth = calendar.prmonth(2023, 1)

print(cal_mnth)


###############

cal_yr = calendar.calendar(2023)

print(cal_yr)

######
# set num of month per column

cal_out = calendar.calendar(2023, c=5, m=2)

print(cal_out)

######
# set first day as Saturday

calendar.setfirstweekday(calendar.SATURDAY)

print(calendar.month(2023, 1))

#######
# change locale month representation


# ltc_de = calendar.LocaleTextCalendar(locale='de_de')

# print(ltc_de.formatmonth(2019, 1))

# ltc_ja = calendar.LocaleTextCalendar(locale='ja_jp')

# print(ltc_ja.formatmonth(2019, 1))


###################
# represent calendar as HTML

html_cal = calendar.HTMLCalendar()

print(html_cal.formatmonth(2023, 1, withyear=False))
# TODO showcase: save html and open it in browser
print('#########################')
print(html_cal.formatyear(2023, width=5))
# TODO showcase: save html and open it in browser
###
print(html_cal.cssclasses)
# Todo: add more pop names to weekdays (from songs, movies, etc)
html_cal.cssclasses = ['manic_monday', 'ruby_tuesday', 'wednesday_adams', 'black_thursday', 'good_friday', 'saturday', 'sunday_bloody_sunday'] 

print(html_cal.cssclasses)

####

html_cal_day = calendar.HTMLCalendar(firstweekday=5)
print(html_cal_day.formatmonth(2023, 1))
# again, save html and output in browser

# #### change locale
# lhc = calendar.LocaleHTMLCalendar(firstweekday=6, locale='ja_jp')

# print(lhc.formatmonth(2019, 1))

#### Calendars as lists
import pprint
pprint.pprint(calendar.monthcalendar(2023, 1))

##
calendar.setfirstweekday(5)

pprint.pprint(calendar.monthcalendar(2023, 1))

###

caldr = calendar.Calendar(firstweekday=5)
pprint.pprint(caldr.monthdayscalendar(2023, 1))
print('##########')
pprint.pprint(caldr.yeardayscalendar(2023), depth=3)
print('##########')

pprint.pprint(caldr.yeardayscalendar(2023, width=5), depth=3)


#### get cal as list of tuples

pprint.pprint(caldr.monthdays2calendar(2023, 1))

pprint.pprint(caldr.monthdatescalendar(2023, 1))

# type on the command line:
# python3 -m calendar 2023 1
# python3 -m calendar -h
