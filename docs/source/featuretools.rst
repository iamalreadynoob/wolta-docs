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