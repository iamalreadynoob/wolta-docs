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


load_by_parts
_______________

It enables to load multiple subsets of a dataset into a big one with extensive options.

=================    ========    =============
Parameters           Datatype    Default Value
=================    ========    =============
paths                list        -
strategy             string      default
deleted_columns      list        None
print_description    boolean     False
shuffle              boolean     False
encoding             string      utf-8
=================    ========    =============

.. note::
    strategy can have two different values: 'default' and 'efficient'. The only difference between them is that efficient detects datatypes by using calculate_bounds function. It is not suggested if it is not strictly required.

.. note::
    encoding can have all valid values for encoding parameter of the pandas' read_csv function.

====================    =======    ================    =========
Priority (in return)    Returns    Datatype            Condition
====================    =======    ================    =========
1                       df         pandas dataframe    always
====================    =======    ================    =========

create_chunks
_______________

It splits the dataset into small csv files.

=================    ========    =============
Parameters           Datatype    Default Value
=================    ========    =============
path                 string      -
sample_amount        integer     -
target_dir           string      None
print_description    boolean     False
chunk_name           string      part
=================    ========    =============

.. attention::
    This function does not return any value as result.

transform_data
________________

It transforms data by using some predetermined techniques. Further reading, you may read :ref:`transformation` article.

==========    =======================    =============
Parameters    Datatype                   Default Value
==========    =======================    =============
X             multi dimensional array    -
y             1D array                   -
strategy      string                     log-m
==========    =======================    =============

.. note::
    strategy can have these values: 'log', 'log-m', 'log2', 'log2-m', 'log10', 'log10-m', 'sqrt', 'sqrt-m', 'cbrt'

====================    =======    =======================    =====================
Priority (in return)    Returns    Datatype                   Condition
====================    =======    =======================    =====================
1                       X          multi dimensional array    always
2                       y          1D array                   always
3                       amin_x     integer or float           strategy ends with -m
4                       amin_y     integer or float           strategy ends with -m
====================    =======    =======================    =====================

transform_pred
_______________

It may seem like a reverse function for transform_data. For further reading, you may read :ref:`transformation` article.

==========    ================    =============
Parameters    Datatype            Default Value
==========    ================    =============
y_pred        1D array            -
strategy      string              log-m
amin_y        integer or float    0
==========    ================    =============

.. note::
    strategy can have these values: 'log', 'log-m', 'log2', 'log2-m', 'log10', 'log10-m', 'sqrt', 'sqrt-m', 'cbrt', 'cbrt-m'

====================    =======    ========    =========
Priority (in return)    Returns    Datatype    Condition
====================    =======    ========    =========
1                       y_pred     1D array    always
====================    =======    ========    =========

make_categorical
____________________

It turns continuous values into discrete ones by using normal distribution. The function separates three groups the given data with this approach. For further reading, you may read :ref:`distribution` article.

==========    ========    =============
Parameters    Datatype    Default Value
==========    ========    =============
y             1D array    -
strategy      string      normal
==========    ========    =============

.. note::
    strategy can have these values: 'normal' and 'normal-extra'.

is_normal
______________

It controls that given set behaves like normal distribution or not.

==========    ========    =============
Parameters    Datatype    Default Value
==========    ========    =============
y             1D array    -
==========    ========    =============

====================    =======    ========    =========
Priority (in return)    Returns    Datatype    Condition
====================    =======    ========    =========
1                       result     boolean     always
====================    =======    ========    =========
