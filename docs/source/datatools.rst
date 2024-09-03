Data Tools
===========

This part of the library is designed for data analysis and data manipulation.

col_types
__________

The function gets information about datatypes for each column inside the dataframe.

=============       ================    ==============
Parameters          Datatype            Default Value
=============       ================    ==============
df                  pandas dataframe    -
print_columns       boolean             False
=============       ================    ==============

.. attention::
    It prints out the results if print_columns is True.

====================    =======    ========    =========
Priority (in return)    Returns    Datatype    Condition
====================    =======    ========    =========
1                       types      list        always
====================    =======    ========    =========


unique_amounts
__________

The function gets info about unique value amounts for each column inside the dataframe.

==========    ================    =============
Parameters    Datatype            Default Value
==========    ================    =============
df            pandas dataframe    -
strategy      list                None
print_dict    boolean             False
==========    ================    =============

.. attention::
    If only requested columns are wanted to be examined, then they must be indicated inside the strategy list. Also, it prints out the results if print_dict is True.

====================    =======    ========    =========
Priority (in return)    Returns    Datatype    Condition
====================    =======    ========    =========
1                       space      dict        always
====================    =======    ========    =========


make_numerics
__________

This function converts categorical data to numerical data.

===============    ========    =============
Parameters         Datatype    Default Value
===============    ========    =============
column             1D array    -
space_requested    boolean     False
===============    ========    =============

====================    =======    ========    =======================
Priority (in return)    Returns    Datatype    Condition
====================    =======    ========    =======================
1                       column     1D array    always
2                       space      dict        space_requested is True
====================    =======    ========    =======================


scale_x
________

It scales input values by using Sklearn's Standard Scaler.

==========    =======================    =============
Parameters    Datatype                   Default Value
==========    =======================    =============
X_train       multi dimensional array    -
X_test        multi dimensional array    -
==========    =======================    =============

====================    =======    =======================    =========
Priority (in return)    Returns    Datatype                   Condition
====================    =======    =======================    =========
1                       X_train    multi dimensional array    always
2                       X_test     multi dimensional array    always
====================    =======    =======================    =========

examine_floats
_______________

It examines requested columns that are pre-accepted as float if they have only integer values or not.

=============    ================    =============
Parameters       Datatype            Default Value
=============    ================    =============
df               pandas dataframe    -
float_columns    list                -
get              string              float
=============    ================    =============

.. hint::
    float_columns contains the names of the columns that will be checked by the algorithm.

.. hint::
    get may take two different values: 'float' and 'int'. If it equals to float, it returns non-integer column names. Unless, it returns integer column names.

====================    =======    ========    =========
Priority (in return)    Returns    Datatype    Condition
====================    =======    ========    =========
1                       space      list        always
====================    =======    ========    =========


calculate_bounds
_________________

It returns required datatypes to hold values according to the max and min values.

.. note::
    Sometimes datasets can be huge for our system's capabilities. At this point, decreasing the required space might be essential. This function is designed with this purpose.

.. tip::
    At this rate, I also suggest you use Dask library to get better results.

==========    ============    =============
Parameters    Datatype        Default Value
==========    ============    =============
gen_types     list            -
min_val       int or float    -
max_val       int or float    -
==========    ============    =============

.. hint::
    gen_types can be easily obtained by using col_types function.

====================    =======    ========    =========
Priority (in return)    Returns    Datatype    Condition
====================    =======    ========    =========
1                       types      list        always
====================    =======    ========    =========

calculate_min_max
__________________

It provides very detailed information about min values, max values and datatypes for each column.

.. note::
    This function might be beneficial because it is designed with an approach that does not load all data into memory at once if the device is incapable of doing this.

.. hint::
    The separation into multiple small data files is suggested for the dataset. In further, you may use Glob library in order to obtain paths easily.

===============    ========    =============
Parameters         Datatype    Default Value
===============    ========    =============
paths              list        -
deleted_columns    list        None
===============    ========    =============

.. attention::
    The indicated columns inside deleted_columns will be excluded during the process.

====================    =======    ========    =========
Priority (in return)    Returns    Datatype    Condition
====================    =======    ========    =========
1                       columns    list        always
2                       columns    list        always
3                       max_val    list        always
4                       min_val    list        always
====================    =======    ========    =========

