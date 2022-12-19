#input parameters: dataframe (`df`), list of column names (`cols`), and unit of datetime ('unit')
#logics: convert all columns in `cols` into datetime
#output parameters: transformed dateframe

def convert_to_date(df, cols:list, unit):

    """Convert specified columns from a Pandas dataframe into datetime

    Parameters
    ----------
    df : pd.DataFrame
        Input dataframe
    cols : list
        List of columns to be converted
    unit : string, dafault 'ns'
        available units are 'D', 's', 'ms', 'us', 'ns'

Returns
    -------
    pd.DataFrame
        Pandas dataframe with converted columns
    """

    import pandas as pd
    
    for col in cols:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col],unit=unit)
    return df