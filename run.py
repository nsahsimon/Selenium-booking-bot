from booking.booking import Booking

# going to first page without using instance managers
    # inst = Booking()
    # inst.land_first_page()

# going to first page with instance manager
with Booking(teardown=False) as bot:
    try:
        bot.land_first_page()

    except:
        print("bot instance no longer exists")

    print("exiting....")