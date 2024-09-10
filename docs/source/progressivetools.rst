Progressive Tools
===================

This part of the library is designed for progressive learning.

make_run
___________

It creates multiple models and calculates the accuracy for each one of them, the size of the train data is repeatedly getting bigger till the dedicated size.

===========    ======================    =============
Parameters     Datatype                  Default Value
===========    ======================    =============
model_class    any AI model class        -
X_train        multidimensional array    -
y_train        1D array                  -
X_test         multidimensional array    -
y_test         1D array                  -
init_per       integer                   1
limit_per      integer                   100
increment      integer or float          1
metrics        list                      None
average        string                    weighted
params         dict                      None
===========    ======================    =============

.. note::
    init_per must be less than limit_per.

These are the valid keywords for metrics:

=========    ===============    ==============================
algo_type    metrics keyword    sklearn function
=========    ===============    ==============================
clf          acc                accuracy_score
clf          f1                 f1_score
clf          hamming            hamming_loss
clf          jaccard            jaccard_score
clf          log                log_loss
clf          mcc                matthews_corrcoef
clf          precision          precision_score
clf          recall             recall_score
clf          zol                zero_one_loss
reg          var                explained_variance_score
reg          max                max_error
reg          var                explained_variance_score
reg          abs                mean_absolute_error
reg          sq                 mean_squared_error
reg          rsq                root_mean_squared_error
reg          log                mean_squared_log_error
reg          rlog               root_mean_squared_log_error
reg          medabs             median_absolute_error
reg          poisson            mean_poisson_deviance
reg          gamma              mean_gamma_deviance
reg          per                mean_absolute_percentage_error
reg          d2abs              d2_absolute_error_score
reg          d2pin              d2_pinball_score
reg          d2twe              d2_tweedie_score
=========    ===============    ==============================

.. attention::
    average value must be valid for sklearn's metrics functions.

.. note::
    params is for the model, model does not have to be created in default settings, it can be manipulated.

====================    ==============    ========    =========
Priority (in return)    Returns           Datatype    Condition
====================    ==============    ========    =========
1                       percentage_log    list        always
2                       metrics_log       list        always
====================    ==============    ========    =========

get_best_model
_________________

It calculates the optimum dataset size for the model.

=================    ========    =============
Parameters           Datatype    Default Value
=================    ========    =============
percentage_log       list        -
metrics_log          list        -
requested_metrics    string      -
=================    ========    =============

====================    ===============    ================    =========
Priority (in return)    Returns            Datatype            Condition
====================    ===============    ================    =========
1                       best_percentage    integer or float    always
2                       best_score         float               always
====================    ===============    ================    =========

path_chain
_____________

Sometimes, train data can be kept in different files with different sizes. It is preferred when the data is too big to store in RAM. That function is designed for these situations.

=============    ======================    =============
Parameters       Datatype                  Default Value
=============    ======================    =============
paths            list                      -
model_class      any AI model class        -
X_test           multidimensional array    -
y_test           1D array                  -
output_column    string                    -
metrics          list                      None
average          string                    weighted
params           dict                      None
=============    ======================    =============

These are the valid keywords for metrics:

=========    ===============    ==============================
algo_type    metrics keyword    sklearn function
=========    ===============    ==============================
clf          acc                accuracy_score
clf          f1                 f1_score
clf          hamming            hamming_loss
clf          jaccard            jaccard_score
clf          log                log_loss
clf          mcc                matthews_corrcoef
clf          precision          precision_score
clf          recall             recall_score
clf          zol                zero_one_loss
reg          var                explained_variance_score
reg          max                max_error
reg          var                explained_variance_score
reg          abs                mean_absolute_error
reg          sq                 mean_squared_error
reg          rsq                root_mean_squared_error
reg          log                mean_squared_log_error
reg          rlog               root_mean_squared_log_error
reg          medabs             median_absolute_error
reg          poisson            mean_poisson_deviance
reg          gamma              mean_gamma_deviance
reg          per                mean_absolute_percentage_error
reg          d2abs              d2_absolute_error_score
reg          d2pin              d2_pinball_score
reg          d2twe              d2_tweedie_score
=========    ===============    ==============================

.. attention::
    average value must be valid for sklearn's metrics functions.

.. note::
    params is for the model, model does not have to be created in default settings, it can be manipulated.

====================    ===========    ========    =========
Priority (in return)    Returns        Datatype    Condition
====================    ===========    ========    =========
1                       metrics_log    dict        always
====================    ===========    ========    =========
