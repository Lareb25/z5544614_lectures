""" In-class companion codes for Week 8

Datetime indexes
         
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

def mk_df(
        index_col = None,
        parse_dates = None,
        show = False,
        columns = None,
        ):
    """ Returns an example DF

    Notes
    -----
    see `example0` below for an example of how to use `tk_utils.read_csv_str`



    """
    csv_cnts = '''
    date       , open   , high   , low    , close  , volume
    2010-06-29 , 3.80   , 5.00   , 3.51   , 4.78   , 93831500
    2010-06-30 , 5.16   , 6.08   , 4.66   , 4.77   , 85935500
    2010-07-01 , 5.00   , 5.18   , 4.05   , 4.39   , 41094000
    2010-07-02 , 4.60   , 4.62   , 3.74   , 3.84   , 25699000
    2010-07-06 , 4.00   , 4.00   , 3.17   , 3.22   , 34334500
    2010-07-07 , 3.27   , 3.32   , 2.99   , 3.16   , 34608500
    2010-07-08 , 3.22   , 3.50   , 3.11   , 3.49   , 38557000
    2010-07-09 , 3.51   , 3.57   , 3.30   , 3.48   , 20253000
    2010-07-12 , 3.58   , 3.61   , 3.40   , 3.41   , 11012500
    2010-07-13 , 3.47   , 3.72   , 3.38   , 3.62   , 13400500
    2020-11-02 , 394.00 , 406.98 , 392.30 , 400.51 , 29021100
    2020-11-03 , 409.73 , 427.77 , 406.69 , 423.90 , 34351700
    2020-11-04 , 430.62 , 435.40 , 417.10 , 420.98 , 32143100
    2020-11-05 , 428.30 , 440.00 , 424.00 , 438.09 , 28414500
    2020-11-06 , 436.10 , 436.57 , 424.28 , 429.95 , 21706000
    2020-12-23 , 632.20 , 651.50 , 622.57 , 645.98 , 33173000
    2020-12-24 , 642.99 , 666.09 , 641.00 , 661.77 , 22865600
    2020-12-28 , 674.51 , 681.40 , 660.80 , 663.69 , 32278600
    2020-12-29 , 661.00 , 669.90 , 655.00 , 665.99 , 22910800
    '''
    kargs = {}
    if index_col is not None:
        kargs['index_col'] = index_col
    if parse_dates is not None:
        kargs['parse_dates'] = parse_dates

    df = tk_utils.read_csv_str(csv_cnts, **kargs) 

    if columns is not None:
        df = df.loc[:, columns]

    if show is True:
        info = tk_utils.get_df_info(df)
        printit(
            f"df = mk_df(**{kargs})",
            'df is',
            df,
            '',
            'df.info() gives',
            info,
            )

    return df

def example0(show_desc = True):
    """ Example: The tk_utils.read_csv_str function
    """
    desc = f'''
        example0: The tk_utils.read_csv_str function

        Review: The pandas.read_csv function

        If `loc` is a variable pointing to the location of a CSV file in your
        computer, then

            df = pd.read_csv(loc)

        will create a DF with the data included in this CSV file.

        Suppose we want to create a DF from the data included in a string:

            cnts = """
            date       , open   , high   , low    , close  , volume
            2010-06-29 , 3.80   , 5.00   , 3.51   , 4.78   , 93831500
            2010-06-30 , 5.16   , 6.08   , 4.66   , 4.77   , 85935500
            2010-07-01 , 5.00   , 5.18   , 4.05   , 4.39   , 41094000
            2010-07-02 , 4.60   , 4.62   , 3.74   , 3.84   , 25699000
            """

        In this case, `cnts` points to a string which looks like the content
        of a CSV file. 

        Importantly, this string is NOT the location of a CSV file.

        What if we passed `cnts` as the first parameter or pandas.read_csv?

            df = pd.read_csv(cnts)

        Pandas will raise an exception because it is expecting the location of
        a file, not a string that looks like the contents of a CSV file.

        The function `tk_utils.read_csv_str` works like `pandas.read_csv`,
        except that it expects a string with CSV-formatted data (instead of
        the location of a CSV file)

            df = tk_utils.read_csv_str(cnts)

        '''

    if show_desc is True:
        printit(desc, add_sep=True)

    cnts = '''
        date       , open   , high   , low    , close  , volume
        2010-06-29 , 3.80   , 5.00   , 3.51   , 4.78   , 93831500
        2010-06-30 , 5.16   , 6.08   , 4.66   , 4.77   , 85935500
        2010-07-01 , 5.00   , 5.18   , 4.05   , 4.39   , 41094000
        2010-07-02 , 4.60   , 4.62   , 3.74   , 3.84   , 25699000
        '''
    # NOTE: We are calling the tk_utils.read_csv_str function

    printit(
            '''
            If `cnts` is
            ''',
            cnts,
            '''
            Then tk_utils.read_csv_str(cnts) returns
            ''',
            tk_utils.read_csv_str(cnts),
            '''
            We can any optional parameter accepted by pd.read_csv

            tk_utils.read_csv_str(cnts, index_col='date') returns
            ''',
            tk_utils.read_csv_str(cnts, index_col='date'),
            '',
            show_type=True)

def example1(show_desc = True):
    """ Example: The tk_utils.get_df_info function
    """
    df = mk_df()
    info = tk_utils.get_df_info(df)

    desc = f'''
        example1: The tk_utils.get_df_info function

        This function behaves like df.info() but instead of writing the
        information to the standard output (i.e., "printing it") it returns
        a string with the information from df.info()

        Example:

        Create an example DF using mk_df() above

            df = mk_df()
        
        Use the tk_utils.get_df_info function to save the output of df.info()

            info = tk_utils.get_df_info(df)

        This means that `info` is bound to a string and nothing has been
        "printed" yet
        '''

    if show_desc is True:
        printit(
                desc, 
                '''
                print(info) gives
                ''',
                info,
                '',
                add_sep=True)

def example2(show_desc = True):
    """ Example: the pandas.to_datetime function
    """
    # Create the example DF
    df = mk_df(show=False)
    info = tk_utils.get_df_info(df)

    if show_desc is True:
        printit(
                f'''
                example2: The DatetimeIndex

                Consider the following DF:

                    df = mk_df()

                Then

                df ->
                ''',
                df,
                '''
                The index of this DF is a RangeIndex (integers)

                df.info() -> 
                ''',
                info,
                )

    printit(
            '''

            The elements of 'date' are strings representing dates

            df.loc[:, 'date']
            ''',
            df.loc[:, 'date'],
            '''
            Note the dtype of this series is 'object'

            What if we want to convert these strings to datetime?

            You can use the function pandas.to_datetime to do that
            ''',
            )

    # Create a new series with datetime instances instead of string
    ser = pd.to_datetime(df.loc[:, 'date'])

    printit(
            '''
            ser = pd.to_datetime(df.loc[:, 'date'])
            ser ->
            ''',
            ser,
            )

    comments = '''
    A few comments about this new series:

    1.  The dtype is 'datetime64[ns]'

        This means that the elements of this series will behaver like
        'datetime' instances.

        NOTE: Pandas has its own version of "datetime" objects. In the example
        above, each element is an instance of a class called `Timestamp`. For
        our purposes, these instances will behave like instances of
        `datetime.datetime`

    2.  The string representation of `df.loc[:, 'date']` looks the same as the
        string representation of this new series. 

        Compare:

            df.loc[:, 'date']

            0     2010-06-29
            ...
            18    2020-12-29
            Name: date, dtype: object

        with

            ser = pd.to_datetime(df.loc[:, 'date'])
            ser ->
            0    2010-06-29
            ...
            18   2020-12-29
            Name: date, dtype: datetime64[ns]

        These series "look" the same but the dtype is different

    3.  Without parameters, the function `pd.to_datetime` will "guess"
        the format used to represent dates as strings.

        Setting the optional parameter `format` will tell pandas to use a
        specific format. This format follows the same rules as
        datetime.strftime

        Since the strings above follow the format '%Y-%m-%d', we could have
        used the following expression instead:

        ser = pd.to_datetime(df.loc[:, 'date'], format='%Y-%m-%d')

    4.  You can use `pd.to_datetime` to convert the elements of 'date' from
        strings to datetime

            df.loc[:, 'date'] = pd.to_datetime(df.loc[:, 'date'])


        Notes: 

            - In previous versions of Pandas, the dtype would change to
              'datetime64[ns]'. This is no longer the case.

            - The current version of pandas will not change the dtype
              of df.loc[:, 'date']

    '''
    df.loc[:, 'date'] = pd.to_datetime(df.loc[:, 'date'])
    printit(
            comments,
            '''
            df.loc[:, 'date'] = pd.to_datetime(df.loc[:, 'date'])
            df.loc[:, 'date'] -> 
            ''',
            df.loc[:, 'date'],
            )
    comments = '''

    The fact that pandas does not convert the dtype of df.loc[:, 'date']
    can be confusing.

    One alternative is to convert (or case) the dtype of the column 'date', 
    which will automatically call the pd.to_datetime:

    Alternative 1:

        df = mk_df()  # New DF
        # Change the elements of the column 'date' but not the dtype
        df.loc[:, 'date'] = pd.to_datetime(df.loc[:, 'date'])


    Alternative 2:

        df = mk_df()  # New DF
        # Change the elements and the dtype
        df = df.astype({'date': 'datetime64[ns]'})

    '''

    printit(
            comments,
            )

    # Implement alternative 2
    df = mk_df()
    df = df.astype({'date': 'datetime64[ns]'})
    info = tk_utils.get_df_info(df)
    printit(
            '''
            Implementing alternative 2

            df = mk_df()
            df = df.astype({'date': 'datetime64[ns]'})

            df -> 
            ''',
            df,
            '''
            df.info() ->
            ''',
            info,
            )

def example3(show_desc = True):
    """ Example: Automatic conversion using pandas.read_csv
    """
    cnts = '''
        date       , open   , high   , low    , close  , volume
        2010-06-29 , 3.80   , 5.00   , 3.51   , 4.78   , 93831500
        2010-06-30 , 5.16   , 6.08   , 4.66   , 4.77   , 85935500
        2010-07-01 , 5.00   , 5.18   , 4.05   , 4.39   , 41094000
        '''


    desc = f'''
    The function `pandas.read_csv` accepts an optional parameter called

        parse_dates

    You can set this parameter to the list of columns you want pandas to
    convert to datetime64[ns]

    In this example, we will use the function `tk_utils.read_csv_str` to
    demonstrate how this works.

    Suppose you have 

        cnts = """{cnts}"""

    Then df = tk_utils.read_csv_str(cnts) will create a new DF

    The type of the column df.loc[:, 'date'] is object and its elements are
    strings

    '''

    if show_desc is True:
        printit(desc, add_sep=True)


    # Without the parse_dates parm
    df = tk_utils.read_csv_str(cnts)
    printit(
            '''
            df = tk_utils.read_csv_str(cnts)
            df.loc[:, 'date'] ->
            ''',
            df.loc[:, 'date'],
            '''
            df.loc[:, 'date'].dtype is object
            ''',
            )

    # With the parse_dates parm
    df = tk_utils.read_csv_str(cnts, parse_dates=['date'])

    printit(
            '''
            Alternatively, set `parse_dates`

            df = tk_utils.read_csv_str(cnts, parse_dates=['date'])
            df.loc[:, 'date'] -> 
            ''',
            df.loc[:, 'date'],
            '''
            df.loc[:, 'date'].dtype is datetime64[ns]
            ''',
            )

def example4(show_desc = True):
    """ Example: Intro to DatetimeIndex
    """
    # Construct an example DF
    df = mk_df(parse_dates=['date'])
    info = tk_utils.get_df_info(df, indent=' '*8).lstrip()

    desc = f'''
    Start with a new DF, with df.loc[:, 'date'].dtype as 'datetime64[ns]'

    We will use the function `mk_df` to construct this DF

        df = mk_df(parse_dates=['date'])

        df.info() gives

        {info}

    '''
    if show_desc is True:
        printit(desc, add_sep=True)

    df.set_index('date', inplace=True)

    printit(
            '''
            Set the index to 'date'
            df.set_index('date', inplace=True)
            
            df.info() -> 
            ''',
            tk_utils.get_df_info(df),
            '''
            Note that the index is `DatetimeIndex`

            If you print the DF, it will look like a string index

            df ->
            ''',
            df,
            '''
            Similarly, the elements of the index look like strings

            df.index ->
            ''',
            df.index,
            '''
            But the dtype of the index is 'datetime64[ns]'
            This means that its elements are Timestamp instances!

            df.index[0] -> 
            ''',
            df.index[0],
            '''
            Again, Timestamp instances behave like datetime.datetime instances
            ''',
            )
    comment = '''
    Why not use Index with dtype='datetime64[ns]'?

    What makes a DatetimeIndex special?

    The answer is that the DatetimeIndex objects behave differently than Index
    objects.

    See examples below

    '''
    printit(comment)

def example5(show_desc = True):
    """ Example: Working with DatetimeIndex indexes (I)
    """
    # Construct an example DF and set the index to DatetimeIndex
    df = mk_df(parse_dates=['date'], index_col='date')
    info_dt = tk_utils.get_df_info(df, indent=' '*8).lstrip()

    df_nodt = mk_df(index_col='date')
    info_nodt = tk_utils.get_df_info(df_nodt, indent=' '*8).lstrip()

    desc = f'''
    example5: Working with DatetimeIndex indexes (I)

    We will use the function `mk_df` to construct two DFs: One with a
    DatetimeIndex and the other with a normal Index including strings

        # This dataframe includes a DatetimeIndex
        df = mk_df(parse_dates=['date'], index_col='date')

        # This dataframe has a normal index
        df_nodt = mk_df(index_col='date')

        df.info() gives

        {info_dt}

        whereas df_nodt.info() gives

        {info_nodt}


    '''
    if show_desc is True:
        printit(
                desc, 
                '''
                Note the indexes look the same but they are not

                df.index ->
                ''',
                df.index,
                '''
                df_nodt.index ->
                ''',
                df_nodt.index,
                add_sep=True)

    printit(
            f'''

            Last week, we saw that the following will result in an exception

                df_nodt.loc['2020'] -> KeyError: '2020'

            This is because '2020' is not a label in the Index `df_nodt`

            However, when the index is a DatetimeIndex, we can pass strings
            representing parts of the date:

            The following will return all dates in DatetimeIndex
            with year = 2020

            df.loc['2020'] ->
            ''',
            df.loc['2020'],
            '''
            Similarly, the following will return all dates in 
            November of 2020

            df.loc['2020-11'] ->
            ''',
            df.loc['2020-11'],
            '''
            You can also use slices with partial dates
            df.loc['2020-11':'2020-12-23'] ->
            ''',
            df.loc['2020-11':'2020-12-23'],
            )

def example6(show_desc = True):
    """ Example: Computing returns
    """
    # Construct an example DF and set the index to DatetimeIndex
    # We only want one column: 'close'
    df = mk_df(parse_dates=['date'], index_col='date', columns=['close'])
    info = tk_utils.get_df_info(df, indent=' '*8).lstrip()

    if show_desc is True:
        printit(
                f'''
                example6: Computing returns

                Create a DF with a DatetimeIndex index and a single column
                with closing prices

                    df = mk_df(parse_dates=['date'], index_col='date')

                    {info}

                This DF looks like this:

                ''',
                df,
                '''
                Note that there are gaps in this time-series

                In particular, a big gap from 2020-07-14 to 2020-11-01
                ''',
                add_sep=True)

    printit(
            '''
            We can use the series method .pct_change to calculate returns

            If `ser` is a series with a normal index, this method will create
            another series using the formula similar to:

                ser.iloc[i] - ser.iloc[i-1]
                ---------------------------
                    ser.iloc[i-1]

            where the result will be NAN if this ratio cannot be computed 

            With a DatetimeIndex, this is also the default behavior.

            The following will compute returns using the values in 'close'

                rets = df.loc[:, 'close'].pct_change()

            rets ->

            ''',
            df.loc[:, 'close'].pct_change(),
            '''
            Note that the first element of the series is NAN because we need
            at least one lagged value to compute pct_change

            Also, note that pandas does not care if there are gaps in the 
            series.

            If your goal was to compute "daily" returns, this is not the 
            right way to do it. This is because the return on 2020-11-02
            is the return over almost 10 years.

            However, the pct_change method accepts an optional parameter
            called

                freq

            This tells pandas the frequency of this time series 
            (assuming we have a DatetimeIndex)

            For daily frequency, use `freq='D'`

            Let's try 

                rets = df.loc[:, 'close'].pct_change(freq='D')

            rets ->

            ''',
            df.loc[:, 'close'].pct_change(freq='D'),
            '''
            Note that pandas will only compute returns if prices from
            consecutive days are available. 

            This solves the problem of the 10-year gap. However, returns 
            from Friday to Monday will all be set to NaN

            Instead of calendar days, we can set the frequency to "Business
            days" by setting `freq='B'`

            Let's try 

                rets = df.loc[:, 'close'].pct_change(freq='B')

            rets ->
            ''',
            df.loc[:, 'close'].pct_change(freq='B'),
            '''
            This helps but it does not take into account holidays.

            You can create a custom calendar that excludes holidays. 
            We will not discuss this method because there is an easier way to
            do the same thing:

            1.  Create a series which includes all "TRADING DAYS". This will
                ensure that pandas only counts the days a particular 
                exchange is open.

            2.  "Left-join" this series with any price series. We will learn
                how to perform these joins next week

            3.  Compute returns using `.pct_change` without a value for `freq`


            We will talk more about this later in the course

            ''',

            )




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
            ]

    #  run examples
    for func in examples_to_run:
        func(show_desc=show_desc)

if __name__ == "__main__":
    main()
