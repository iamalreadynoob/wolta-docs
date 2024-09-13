Feature Tools
===============

This part of the library is designed for feature selection.

quest_selection
_________________

It follows these instructions:

1. Calculate the accuracy without feature selection, if it was not calculated.
2. In each iteration, ignore one feature. For all features, do it. After that, calculate the new accuracy. If it is greater than or equal to the general accuracy or the difference between them is smaller than or equal to flag_one_tol, then take this feature to the next step.
3. Create random combinations with these features and calculate the new accuracy. If one of the combinations provides an accuracy that is greater than or equal to general accuracy or their difference is smaller than or equal to fin_tol, then print it out to the console.

============    ======================    =============
Parameters      Datatype                  Default Value
============    ======================    =============
model_class     any AI model class        -
X_train         multidimensional array    -
y_train         1D array                  -
X_test          multidimensional array    -
y_test          1D array                  -
features        list                      -
flag_one_tol    float                     -
fin_tol         float                     -
params          dict                      None
normal_acc      float                     None
trials          integer                   100
============    ======================    =============

.. note::
    features need to contain the names of the columns in X array.

.. note::
    params is for the model, model does not have to be created in default settings, it can be manipulated.

.. note::
    normal_acc is the accuracy score for dataset without feature selection.

.. attention::
    trials dedicates the third step to how many times it will be repeated.

.. note::
    This function only prints out to the console, nothing returns.

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
