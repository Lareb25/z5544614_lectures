""" In-class companion codes for Week 8

The datetime module

         
"""


import datetime as dt

import pandas as pd

import tk_utils
import toolkit_config as cfg


def printit(*args, 
            add_sep = False,
            show_type = False,
            show_id = False,
            dedent = True,
            ):
    """ Run utils.printit function with other defaults
    """
    tk_utils.printit(*args, add_sep=add_sep, show_type=show_type,
                     show_id=show_id, dedent=dedent)


def example0(show_desc = True):
    """ Example: The datetime module
    """
    if show_desc is True:
        printit(
                f'''
                example0: The datetime module

                The datetime module defines a number of classes, including

                  datetime -> objects representing date + time     
                  timedelta -> objects representing intervals

                The convention is to to import the datetime module as dt:

                    import datetime as dt

                Therefore:

                    dt.datetime  -> <class datetime.datetime>
                    dt.timedelta -> <class datetime.timedelta>

                Intuitively, python will evaluate `dt.timedelta` as follows

                From left to right:

                1.  It the name `dt` bound to an object? Yes, the `datetime`
                    module. So "replace" `dt` with the module object `datetime`. 

                2.  Is the name `timedelta` available in the `datetime`
                    module's namespace? Yes, it refers to the class object
                    `datetime.timedelta`.

                3.  The result is that `dt.timedelta` will be "replaced" with
                    the class object `datetime.timedelta` currently in memory

                ''',
                add_sep=True)

    exercise0 = '''
    Exercise: Use `str` to display the string representation of the
    following objects:
    
    1. The module `datetime`
    2. The class `datetime` defined in the module `datetime` 
    3. The class `timedelta` defined in the module `datetime`
    '''
    printit(exercise0, add_sep=True)
    # <COMPLETE THIS PART>



    exercise1 = '''
    Answer the following questions:

    1. Does `dt.datetime` refer to an INSTANCE of `datetime.datetime`?
    
    '''
    printit(exercise1, add_sep=True)
    # <COMPLETE THIS PART>




def example1(show_desc = True):
    """ Example: The class method datetime.datetime.now 
    """
    if show_desc is True:
        printit(

                '''
                example1: The datetime.datetime.now class method

                Intuitively, we have:

                datetime module             <- Module
                    
                    datetime class          <- Inside datetime module

                        now class method    <- Inside datetime.datetime class

                Normally, functions defines inside classes become instance
                methods.

                However, classes can also define class methods (instead of
                class functions)

                    These are meant to be called using the class, instead of
                    the instance

                    Unlike class functions, the first parameter is not meant
                    to be an instance of that class

                The class method `now` can be accessed as follows:

                    import datetime as dt
                    dt.datetime.now 


                Breaking down `dt.datetime.now`

                    dt -> <module 'datetime'>

                    dt.datetime -> <class 'datetime.datetime'>

                    dt.datetime.now -> <built-in method now of type object at ...>

                Note that `dt.datetime.now` is a method, not a function!

                ''',
                add_sep=True)

    exercise0 = '''
    Exercise: What is the string representation of the 
    objects assigned to:

        dt
        dt.datetime
        dt.datetime.now
    '''
    printit(exercise0, add_sep=True)
    # <COMPLETE THIS PART>

    # <solution>
    print(dt)               # <module 'datetime'>
    print(dt.datetime)      # <class 'datetime.datetime'>
    print(dt.datetime.now)  # <built-in method now of type object at ...>
    # </solution>

    exercise1 = '''
    Exercise: Use the help function to find more about dt.datetime.now
    '''
    printit(exercise1, add_sep=True)
    # <COMPLETE THIS PART>

    # <solution>
    # NOTE: The builtin help function works great but it stops the execution
    # of the code (because it essentially starts an interactive shell)
    # Alternatively, you could use the function:
    #
    #   tk_utils.help(obj)
    #
    # which returns a STRING with the documentation for that function
    #
    print(tk_utils.help(dt.datetime.now))               # <module 'datetime'>
    # </solution>

def example2(show_desc = True):
    """ Example: Creating and representing dates using datetime.datetime.now
    """
    if show_desc is True:
        printit(

                '''
                example2: Creating and representing dates using datetime.datetime.now

                We typically call this method without any parameters

                    import datetime as dt

                    dt.datetime.now() -> Instance of datetime.datetime 

                This method returns an instance of `datetime.datetime` with
                the current date and time

                ''',
                add_sep=True)

    # Create an instance
    dt_now = dt.datetime.now()

    printit(
            f'''
            Create an instance of datetime.datetime with the current date/time

            dt_now = dt.datetime.now()

            What is the string representation of this object?

            str(dt_now) ->
            ''',
            str(dt_now),
            f'''
            The class datetime.datetime decides how instances will be
            represented as strings. The default is represent the underlying
            date/time in ISO format:

            YYYY-MM-DD HH:MM:SS.MS

            where
                YYYY: 4-digit year
                MM: 2-digit month
                DD: 2-digit day
                HH: Hour (24h format)
                MM: Minutes
                SS: Seconds
                MS: Microsecond

            This is a very convenient and user-friendly representation

            However, str(object) is not the only way to represent objects as
            strings. 
            ''',
            )

    
    # --------------------------------------------------------
    #   str vs repr 
    # --------------------------------------------------------
    # Output of help(repr)
    #   First, create a string with the output of help(repr) 
    #   tk_utils(help) -> str with the output of help
    help_repr = tk_utils.help(repr, indent=' '*16)
    printit(
            f'''
            You can also use the built-in function repr(object)

                help(repr) ->

                    {help_repr}

            So, repr(obj) also returns a string representation of the instance
            `obj`

            The main difference between str and repr is that the latter will
            (typically) return a string which could be evaluated as an
            expression to produce that instance. 

            Like `str`, the class decides the output of `repr` so this is not
            always the case. For instance if `ser` is a pandas series, the
            output of `repr(ser)` is the same as `str(ser)`

            For datetime.datetime objects, `repr` returns a string with 
            an expression that is very similar to the one you would use to
            create that instance (the difference is that `datetime` is not 
            abbreviated to `dt`)

            Previously, we created an instance of datetime.datetime using
            the class method `now`:

                dt_now = dt.datetime.now()

            Compare the output of `str(dt_now)` with `repr(dt_now)`

            str(dt_now) ->
            ''',
            str(dt_now),
            '''
            repr(dt_now) ->
            ''',
            repr(dt_now),
            f'''
            The output of `repr(dt_now)` (strongly) suggests how one
            could create an instance of datetime.datetime with the same
            value (i.e., the same date/time) as dt_now:

            dt_now1 = dt.datetime(
                year={dt_now.year}, 
                month={dt_now.month}, 
                day={dt_now.day}, 
                minute={dt_now.minute},
                second={dt_now.second},
                microsecond={dt_now.microsecond},
                )

            Although the parameters are pretty self-explanatory, 
            the documentation of `dt.datetime` provides a lot of important
            additional information
            ''',
            )

    # ----------------------------------------------------     
    #  The output of help(dt.datetime)
    # ---------------------------------------------------- 
    help_datetime = tk_utils.help(dt.datetime, indent=' '*16)
    printit(
            f'''

            help(dt.datetime) ->
                {help_datetime}
                
            ''',
            )

    # ----------------------------------------------------     
    #  Summarizing the help(dt.datetime)
    # ---------------------------------------------------- 
    printit(
            f'''
            The documentation of `datetime.datetime` is long and includes a
            lot of information. 

            For now, here is a summary of what you need to know:

            Parameters:

            - The class `datetime.datetime` takes three mandatory parameters

                - year, month, day

            - Optionally, you can also pass `minute`, `second`, `microsecond`,
              and `tzinfo`

            - `tzinfo` represents timezone information. For our purposes, we
              we will use the local timezone, which is the default.

            Instance attributes:

            You can get the "date" or "time" part of a datetime instance using
            the attributes:

                .year
                .month
                .day
                .minute
                .second
                .microsecond

            A very common and useful instance method:

                strftime: See examples below
            ''',
            )
    exercise0 = '''
    1.  Create an instance of datetime.datetime with your birthday
        and assign it to a variable called `d`

    2.  Print that instance (which calls str(d) internally)
    3.  Print the output of `repr(d)
    4.  Use the instance to print your birth year
    '''
    printit(exercise0, add_sep=True)




def example3(show_desc = True):
    """ Example: The datetime.timedelta class
    """
    if show_desc is True:
        printit(

                '''
                example3: The datetime.timedelta class

                Instances of datetime.timedelta are meant to represent
                periods (e.g, 1 day, 2 mins, 10 secs, etc...)

                As the name suggests, the "delta" (or difference) between two
                datetime instances is represented by a timedelta instance

                To see that, first create two datetime.datetime instances:

                dt0 = dt.datetime(2022, 11, 1) 

                dt1 = dt.datetime(
                    year=2022, 
                    month=11, 
                    day=1, 
                    hour=8,             <- Not the default
                    minute=0,           <- Unnecessary b/c default is 0
                    second=0,           <- Unnecessary b/c default is 0
                    microsecond=0,      <- Unnecessary b/c default is 0
                    )


                ''',
                add_sep=True)

    # Create the two datetime instances (8 hours apart)
    dt1 = dt.datetime(
        year=2022, 
        month=11, 
        day=1, 
        hour=8,             # <- Not the default
        )
    dt0 = dt.datetime(2022, 11, 1)
    # Creates an instance of timedelta 
    elapsed = dt1 - dt0

    printit(
            f'''
            Logically, the difference b/w dt1 and dt0 is 8 hours

                str(dt1) -> 2022-11-01 08:00:00
                str(dt0) -> 2022-11-01 00:00:00

            In Python, the difference of two datetime.datetime objects
            is a datetime.timedelta object

                elapsed = dt1 - dt0

                type(elapsed) -> {type(elapsed)}

            The string representation of this object is a human-friendly
            representation of the elapsed time (i.e., the value of this
            instance):

                str(elapsed) ->  {str(elapsed)}


            This representation will change depending on the length of the
            time interval.

            We can also use repr:

                repr(elapsed) ->  {repr(elapsed)}

            ''',
            )

    # --------------------------------------------------------
    #   Getting help 
    # --------------------------------------------------------
    help_td = tk_utils.help(dt.timedelta, indent=' '*16)
    
    printit(
            f'''
            For more information:

                help(dt.timedelta) ->
                    {help_td}

            As with datetime.datetime, the documentation is long and 
            includes a lot of information.

            In the next examples we will highlight a few important concepts

            ''',

            )


def example4(show_desc = True):
    """ Example: Working with timedelta instances
    """

    # Lets create two other datetime instances:
    #   dt0 --> 2019-12-31 00:00:00
    #   dt1 --> 2020-01-01 08:00:00
    dt0  = dt.datetime(2019, 12, 31)
    dt1  = dt.datetime(2020, 1, 1, hour=8)

    # Operations between datetime objects will return timedelta objects
    elapsed = dt1 - dt0

    if show_desc is True:
        printit(
                f'''
                example4: Working with timedelta instances

                First, create two new datetime instances:

                    dt0  = dt.datetime(2019, 12, 31)
                    dt1  = dt.datetime(2020, 1, 1, hour=8)

                The difference is a timedelta instance representing a 1 day
                and 8-hour interval

                    elapsed = dt1 - dt0
                    str(elapsed) -> {elapsed}

                You can access the "parts" of this time interval using the
                attributes

                    .days         -> number of days
                    .seconds      -> number of seconds (>= 0 and less than 1 day)
                    .microseconds -> microseconds (>= 0 and less than 1 second)

                IMPORTANT: 

                    - There is no "hours" or "minutes" attribute

                        - Even though you can pass hours or minutes as
                          parameters

                    - "seconds" is the number of seconds ON TOP of the number of
                      days

                    - "microseconds" is the number of microseconds ON TOP OF the
                      number of days + seconds

                This means that (logically) the interval is 

                    elapsed.days + elapsed.seconds + elapsed.microseconds

                ''',
                add_sep=True)

    # --------------------------------------------------------
    #  Accessing parts of the interval
    # --------------------------------------------------------
    printit(
            f'''
            For the timedelta object above:

                str(elapsed) -> {elapsed}

            we have:

                elapsed.days -> {elapsed.days}
                elapsed.seconds -> {elapsed.seconds}
                elapsed.microseconds -> {elapsed.microseconds}

            Again, note that elapsed.seconds is NOT the total number of
            seconds in this interval. Instead, it represents the part of this
            interval that is less than N days: 8 hours

                elapsed.seconds/(60*60) -> {elapsed.seconds/(60*60)}

            ''',
            )


    # --------------------------------------------------------
    #   The total_seconds method 
    # --------------------------------------------------------
    printit(
            f'''
            Instances of datetime.timedelta have a useful method called

                .total_seconds()

            When called, this method will return the TOTAL number of seconds
            in the interval represented by the timedelta instance

                str(elapsed) -> {elapsed}

                elapsed.total_seconds() -> {elapsed.total_seconds()}

            Note that this is not the same as:

                elapsed.seconds -> {elapsed.seconds}

            ''',
            )


def example5(show_desc = True):
    """ Example: Combining timedelta and datetime
    """

    # Create a datetime and a timedelta 
    start = dt.datetime(2019, 12, 31)
    delta = dt.timedelta(days=1, hours=8)

    # Adding/subtracting a timedelta to/from a datetime produces another
    # datetime
    end = start + delta

    if show_desc is True:
        printit(
                f'''
                example5: Combining timedelta and datetime

                Adding/subtracting a timedelta to/from a datetime produces
                another datetime.

                For example, create the following instances:

                    start = dt.datetime(2019, 12, 31)
                    delta = dt.timedelta(days=1, hours=8)

                where

                    str(start) -> {start}
                    str(delta) -> {delta}

                ''',
                add_sep=True)

    printit(
            f'''
            Adding a timedelta to a datetime will create a new datetime
            instance.

            Example:

                str(start), type(start) -> {start}, {type(start)}
                str(delta), type(delta) -> {delta}, {type(delta)}

                end = start + delta
                
                str(end), type(end) -> {end}, {type(end)}

            ''',
            )


def example6(show_desc = True):
    """ Example: The .strftime method 
    """
    d = dt.datetime(2020, 11, 3, hour=8)
    help_strftime = tk_utils.help(dt.datetime.strftime, indent=' '*16)

    if show_desc is True:
        printit(
                f'''
                example6: The .strftime method

                The method `.strftime` is available to any instance of
                datetime.datetime. For example:

                    d  = dt.datetime(2020, 11, 3, hour=8)
                    d.strftime -> {d.strftime}

                The purpose of this method is to create custom string
                representations of the datetime instance.


                ''',
                add_sep=True)

    printit(
            f'''
            The method strftime takes one parameter, which tells Python
            how to represent the instance as a string.

            This parameter is a string in which you combine "directives"
            with any other string you want.

            Think of these directives as "macros" representing date formats.

            For instance, the directive %Y represents the year using 4 digits

                str(d) -> {d}
                d.strftime('%Y') -> {d.strftime('%Y')}

            Note that the format may only include a portion of the date.

            The directive %b represents the abbreviated month name, whereas %d
            represents the day using 2 digits. We can combine these directives
            as follows:

                d.strftime('%b %d, %Y') -> {d.strftime('%b %d, %Y')}


            See the Python documentation for a complete list of directives.

            ''',
            )



def example7(show_desc = True):
    """ Exercise
    """
    printit(
            '''
            Exercises: 
            1.  For how many seconds have you been alive?
            2.  How old will you be in 1,340 days?
            ''',
            add_sep=True)

    # <COMPLETE THIS PART>



    # <COMPLETE THIS PART>


def main():
    """
    """
    # Set to False to suppress the example description
    show_desc = True

    examples_to_run = [
            #example0,
            #example1,
            #example2,
            #example3,
            #example4,
            #example5,
            #example6,
            #example7,
            ]

    #  run examples
    for func in examples_to_run:
        func(show_desc=show_desc)

if __name__ == "__main__":
    main()

