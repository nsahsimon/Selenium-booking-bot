from booking.booking import Booking

# going to first page without using instance managers
# inst = Booking()
# inst.land_first_page()

# going to first page with instance manager
with Booking(teardown=False) as bot:
    bot.land_first_page()
    bot.change_currency(currency="USD")
    bot.select_place_to_go()
    bot.select_dates(check_out_date='2023-02-25', check_in_date='2023-02-10' )
    print("exiting....")

