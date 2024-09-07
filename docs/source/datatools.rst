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

seek_null
___________

It checks each column in the dataframe to see if they have null values or not and how many if there are any. After the process it returns a list full of the names of the columns which have null values.

=============    ================    =============
Parameters       Datatype            Default Value
=============    ================    =============
df               pandas dataframe    -
print_columns    boolean             False
=============    ================    =============

.. attention::
    It is visible that how many null values have the columns, when print_columns is True. The values are printed out to the console.

====================    ============    ========    =========
Priority (in return)    Returns         Datatype    Condition
====================    ============    ========    =========
1                       null_columns    list        always
====================    ============    ========    =========

make_null
__________

Sometimes the null values may be represented in different ways (using 'unknown' in string data for example) instead of being null inside the dataset.

==========    ===============================    =============
Parameters    Datatype                           Default Value
==========    ===============================    =============
matrix        pandas dataframe or numpy array    -
replace       anything                           -
type          string                             df
==========    ===============================    =============

.. attention::
    type declares that matrix is a pandas dataframe or numpy array. It has two different valid values, which are 'df' and 'np'. 'df' means pandas dataframe, 'np' means numpy array.

====================    =======    ===============================    =========
Priority (in return)    Returns    Datatype                           Condition
====================    =======    ===============================    =========
1                       matrix     pandas dataframe or numpy array    always
====================    =======    ===============================    =========

stat_sum
_________

It summarises the collected info about dataframe like describe method from Pandas.

==========    ================    =============
Parameters    Datatype            Default Value
==========    ================    =============
df            pandas dataframe    -
requested     list                -
only          list                None
exclude       list                None
get_dict      boolean             False
verbose       boolean             True
==========    ================    =============

.. tip::
    If only is not None, only indicated columns in the list are examined.

.. tip::
    If exclude is not None, all columns except indicated in the list are examined.

Here is the list of valid keywords for requested:

=============    ===============================================================================
Valid Keyword    Meaning
=============    ===============================================================================
all              if the list has it at index zero then it presumes that it contains all keywords
min              minimum
max              maximum
width            the difference between max and min
mean             arithmetic mean
std              standard deviation
med              median
var              variance
=============    ===============================================================================

====================    ===========    ==========    ===================
Priority (in return)    Returns        Datatype      Condition
====================    ===========    ==========    ===================
1                       gen_results    dictionary    if get_dict is True
====================    ===========    ==========    ===================

find_deflection
________________

It analyses the difference between prediction and actual values for regression problems and returns a report about how successful the prediction was.

===============    ================    =============
Parameters         Datatype            Default Value
===============    ================    =============
y_test             1D array            -
y_pred             1D array            -
arr                boolean             True
avg                boolean             False
gap                integer or float    None
gap_type           string              num
dif_type           string              f-i
avg_w_abs          boolean             True
success_indexes    boolean             False
===============    ================    =============

These are the valid keywords for gap_type:

========    ======================================================================
gap_type    succession condition
========    ======================================================================
exact       prediction = actual
num         actual - gap <= prediction <= actual + gap
num+        actual <= prediction <= actual + gap
num-        actual - gap <= prediction <= actual
per         (100 - gap) * actual / 100 <= prediction <= (100 + gap) * actual / 100
per+        actual <= prediction <= (100 + gap) * actual / 100
per-        (100 - gap) * actual / 100 <= prediction <= actual
========    ======================================================================

====================    =========    ========    =======================
Priority (in return)    Returns      Datatype    Condition
====================    =========    ========    =======================
1                       diffs        list        arr is True
2                       avg_score    float       avg is True
3                       succ         integer     gap is not None
4                       indexes      list        success_indexes is True
====================    =========    ========    =======================

.. note::
    diffs is the list full of with the differences between actual and predicted values.

These are the supported methods for difference calculation:

========    ==================================
dif_type    calculation
========    ==================================
f-i         final (prediction) - init (actual)
i-f         init (actual) - final (prediction)
abs         absolute
========    ==================================

.. note::
    avg_score equals the arithmetic mean of the diffs set.

.. note::
    succ is the amount of the succeeded predictions according to the gap condition. indexes hold the index information, which are successful predictions.


extract_float
_______________

Sometimes float data might be held with a different representation ('3.5$' for example). In that case, the unwanted symbols (the dollar sign in this example) can be deleted and the datatype of the list can be converted from string to float.

==========    ========    =============
Parameters    Datatype    Default Value
==========    ========    =============
column        1D array    -
symbols       list        -
==========    ========    =============

====================    =======    ========    =========
Priority (in return)    Returns    Datatype    Condition
====================    =======    ========    =========
1                       column     1D Array    always
====================    =======    ========    =========

list_deletings
_______________

It analyses the dataframe and shows or deletes columns that were found to be improper by the algorithm.

=================    ==================    =============
Parameters           Datatype              Default Value
=================    ==================    =============
df                   pandas dataframe      -
extra                list                  None
del_null             boolean               True
null_tolerance       integer or float      20
del_single           boolean               True
del_almost_single    boolean               False
almost_tolerance     integer or float      50
suggest_extra        boolean               True
return_extra         boolean               False
unique_tolerance     integer or boolean    10
=================    ==================    =============

.. note::
    The column which their names are inside the extra library are deleted directly.

.. note::
    While del_null is true, the columns that have null values greater than null_tolerance% of the total sample amount are deleted.

.. note::
    If del_single is true, then the columns that have only one different value are deleted.

.. note::
    While del_almost_single is true, the columns that have the same value that more than almost_tolerance% of the total sample amount are deleted.

.. note::
    While suggest_extra is true, the string data held columns that have unique values greater than unique_tolerance% of the total sample amount are printed out in the console. The list of columns is also returned if return_extra is true.

====================    =======    ================    ====================
Priority (in return)    Returns    Datatype            Condition
====================    =======    ================    ====================
1                       df         pandas dataframe    always
2                       columns    list                return_extra is True
====================    =======    ================    ====================

col_counts
____________

It returns the frequency of unique values in columns by using value_counts function from pandas.

==========    ================    =============
Parameters    Datatype            Default Value
==========    ================    =============
df            pandas dataframe    -
exclude       list                None
only          list                None
==========    ================    =============

.. tip::
    If only is not None, only indicated columns in the list are examined.

.. tip::
    If exclude is not None, all columns except indicated in the list are examined.

.. attention::
    This function only prints out the result to the console. It does not return anything.

check_similarity
__________________

Sometimes the very same information can be held into two different columns with different representations. For example, the area code information can be stored with digits and their actual names into two different columns, but they hold the same thing.

==========    ========    =============
Parameters    Datatype    Default Value
==========    ========    =============
col1          1D array    -
col2          1D array    -
==========    ========    =============

====================    ==========    ========    =========
Priority (in return)    Returns       Datatype    Condition
====================    ==========    ========    =========
1                       similarity    boolean     always
====================    ==========    ========    =========

.. attention::
    If similarity is true, then it means that these columns have the same information.

find_broke
____________

If the datatype of the column is different than expected, it can be examined by using this method and found the reason.

=============    ========    =============
Parameters       Datatype    Default Value
=============    ========    =============
column           1D array    -
dtype            datatype    float
get_indexes      boolean     True
get_words        boolean     False
verbose          boolean     True
verbose_limit    integer     10
=============    ========    =============

====================    =======    ========    ===================
Priority (in return)    Returns    Datatype    Condition
====================    =======    ========    ===================
1                       indexes    list        get_indexes is True
2                       words      list        get_words is True
====================    =======    ========    ===================

multi_split
____________

It is designed to create different arrays with requested threshold values for train-test splitting.

=============    ================    =============
Parameters       Datatype            Default Value
=============    ================    =============
df               pandas dataframe    -
test_size        float               -
output           string              -
threshold_set    list                -
=============    ================    =============

.. note::
    test_size must be between 0 and 1.

.. attention::
    The very first multidimensional array inside lists is always created without any selection.

.. attention::
    The output arrays are created in order to the order inside threshold_set.

.. attention::
    Output arrays (y_train and y_test) are always the same for every output set. It is because measuring correctly the success rate between different approaches.

====================    ========    ========    =========
Priority (in return)    Returns     Datatype    Condition
====================    ========    ========    =========
1                       X_trains    list        always
2                       X_tests     list        always
3                       y_train     1D array    always
4                       y_test      1D array    always
====================    ========    ========    =========

expand_df
___________

It oversamples the dataset by using SMOTE.

=================    ====================    =============
Parameters           Datatype                Default Value
=================    ====================    =============
df                   pandas dataframe        -
output               string                  -
sampling_strategy    string or dictionary    -
=================    ====================    =============

====================    =======    ================    =========
Priority (in return)    Returns    Datatype            Condition
====================    =======    ================    =========
1                       df         pandas dataframe    always
====================    =======    ================    =========