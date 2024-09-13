Model Tools
=============

This part of the library is designed for model creation and analysing.

get_score
__________

It returns the requested metric scores for the model.

==========    ========    =============
Parameters    Datatype    Default Value
==========    ========    =============
y_test        1D array    -
y_pred        1D array    -
metrics       list        None
average       string      weighted
algo_type     string      clf
verbose       boolean     True
==========    ========    =============

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

.. tip::
    If metrics is empty, for classification acc, for regression sq is printed out.

====================    =======    ==========    =========
Priority (in return)    Returns    Datatype      Condition
====================    =======    ==========    =========
1                       scores     dictionary    always
====================    =======    ==========    =========

do_voting
__________

It is designed to make voting between y_pred arrays which are created by different models for the same test data.

============    ========    =============
Parameters      Datatype    Default Value
============    ========    =============
y_pred_list     list        -
combinations    list        -
strategy        string      avg
============    ========    =============

.. attention::
    combinations is the list of selected indexes for y_pred_list lists. It can be created by using do_combinations functions.

.. note::
    strategy has two valid values: 'avg' and 'mode'. In 'avg' mode, it calculates the mean value and rounds it to an integer value for each prediction. In 'mode' mode, it chooses the most frequent output for each prediction.

====================    =======    ========    =========
Priority (in return)    Returns    Datatype    Condition
====================    =======    ========    =========
1                       results    list        always
====================    =======    ========    =========

.. note::
    It returns the final y_pred arrays inside a list. nth y_pred inside results is always designed for nth index list in combinations.

do_combinations
_________________

It creates combinations due to requested parameters.

==========    ========    =============
Parameters    Datatype    Default Value
==========    ========    =============
indexes       list        -
min_item      integer     -
max_item      integer     -
==========    ========    =============

It makes from min_item selections to max_item selections inside given indexes set.

.. tip::
    This function might be useful for do_voting function.

====================    ============    ========    =========
Priority (in return)    Returns         Datatype    Condition
====================    ============    ========    =========
1                       combinations    list        always
====================    ============    ========    =========

examine_time
_____________

It measures the training time for the given model.

==========    =============================================    =============
Parameters    Datatype                                         Default Value
==========    =============================================    =============
model         any AI model object that has predict function    -
X_train       multidimensional array                           -
y_train       1D array                                         -
==========    =============================================    =============

WelkinClassification
______________________

It is a classification algorithm designed by the developer himself. Further information, visit :ref:`welkin` article.

These are the functions inside the model:

- __init__(strategy='travel', priority=None, limit=None)
- fit(X_train, y_train)
- predict(X_test)

.. note::
    strategy has two valid values: 'travel' and 'limit'.

.. attention::
    priority's datatype is list, limit's datatype is integer. Before changing default settings please read the article mentioned early.

DistRegressor
_______________

It is a regression algorithm designed by the developer himself. Further information, visit :ref:`dist` article.

These are the functions inside the model:

- __init__(verbose=True, clf_model=None, clf_params=None, reg_model=None, reg_params=None, efficiency='time', rus=True)
- fit(X_train, y_train)
- predict(X_test)
- is_data_normal(y)

.. attention::
    Before changing default settings please read the article mentioned early.

compare_models
________________

It is designed to compare models on the same data according to requested metrics.

==========    ======================    =============
Parameters    Datatype                  Default Value
==========    ======================    =============
algo_type     string                    clf
algorithms    list                      -
metrics       list                      -
X_train       multidimensional array    -
y_train       1D array                  -
X_test        multidimensional array    -
y_test        1D array                  -
get_result    boolean                   False
==========    ======================    =============

.. note::
    algo_type has two valid values: 'clf' for classification and 'reg' for regression.

These are the valid keywords for algorithms:

=========    =================    ===============================================================================
algo_type    algorithm keyword    class
=========    =================    ===============================================================================
clf/reg      all                  if the list has it at index zero then it presumes that it contains all keywords
clf          cat                  CatBoostClassifier
clf          ada                  AdaBoostClassifier
clf          dtr                  DecisionTreeClassifier
clf          raf                  RandomForestClassifier
clf          lbm                  LGBMClassifier
clf          ext                  ExtraTreeClassifier
clf          log                  LogisticRegression
clf          knn                  KNeighborsClassifier
clf          gnb                  GaussianNB
clf          rdg                  RidgeClassifier
clf          bnb                  BernoulliNB
clf          svc                  SVC
clf          per                  Perceptron
clf          mnb                  MultinomialNB
reg          cat                  CatBoostRegressor
reg          ada                  AdaBoostRegressor
reg          dtr                  DecisionTreeRegressor
reg          raf                  RandomForestRegressor
reg          lbm                  LGBMRegressor
reg          ext                  ExtraTreeRegressor
reg          lin                  LinearRegression
reg          knn                  KNeighborsRegressor
reg          svr                  SVR
=========    =================    ===============================================================================


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

.. note::
    The function always prints out the results on the console.

====================    =======    ========    ==================
Priority (in return)    Returns    Datatype    Condition
====================    =======    ========    ==================
1                       results    dict        get_result is True
====================    =======    ========    ==================

get_best_model
________________

It gets the best model for the requested metric and trains it. This function can be used with dictionary which is obtained by using compare_models.

==========    ======================    =============
Parameters    Datatype                  Default Value
==========    ======================    =============
scores        string                    clf
rel_metric    list                      -
algo_type     list                      -
X_train       multidimensional array    -
y_train       1D array                  -
behavior      string                    min-best
verbose       boolean                   True
==========    ======================    =============

.. note::
    algo_type has two valid values: 'clf' for classification and 'reg' for regression.

.. note::
    In order to choose the best model rel_metric is the decisive metric inside the results

These are the valid keywords for rel_metric:

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

.. note::
    behavior has two valid values: 'min-best' for minimum score is the best situation and 'max-best' for maximum score is the best situation.

subacc
_________

It calculates the accuracy score for each class independently. It can also return the actual accuracy score if requested.

===========    ========    =============
Parameters     Datatype    Default Value
===========    ========    =============
y_train        1D array    -
y_pred         1D array    -
get_general    boolean     False
===========    ========    =============

====================    ==========    ========    ===================
Priority (in return)    Returns       Datatype    Condition
====================    ==========    ========    ===================
1                       accuracies    dict        always
2                       score         float       get_general is True
====================    ==========    ========    ===================

get_models
____________

It returns requested models in a dictionary after training them.

==========    ======================    =============
Parameters    Datatype                  Default Value
==========    ======================    =============
algorithms    list                      -
X_train       multidimensional array    -
y_train       1D array                  -
==========    ======================    =============

These are the valid keywords for algorithms:

=========    =================    ===============================================================================
algo_type    algorithm keyword    class
=========    =================    ===============================================================================
clf/reg      all                  if the list has it at index zero then it presumes that it contains all keywords
clf          cat                  CatBoostClassifier
clf          ada                  AdaBoostClassifier
clf          dtr                  DecisionTreeClassifier
clf          raf                  RandomForestClassifier
clf          lbm                  LGBMClassifier
clf          ext                  ExtraTreeClassifier
clf          log                  LogisticRegression
clf          knn                  KNeighborsClassifier
clf          gnb                  GaussianNB
clf          rdg                  RidgeClassifier
clf          bnb                  BernoulliNB
clf          svc                  SVC
clf          per                  Perceptron
clf          mnb                  MultinomialNB
reg          cat                  CatBoostRegressor
reg          ada                  AdaBoostRegressor
reg          dtr                  DecisionTreeRegressor
reg          raf                  RandomForestRegressor
reg          lbm                  LGBMRegressor
reg          ext                  ExtraTreeRegressor
reg          lin                  LinearRegression
reg          knn                  KNeighborsRegressor
reg          svr                  SVR
=========    =================    ===============================================================================


====================    =======    ========    =========
Priority (in return)    Returns    Datatype    Condition
====================    =======    ========    =========
1                       models     dict        always
====================    =======    ========    =========

commune_create
________________

It declares the way of commune classification for the given dataset. Further information, please read the :ref:`commune` article.

==========    ======================    =============
Parameters    Datatype                  Default Value
==========    ======================    =============
algorithms    list                      -
X_train       multidimensional array    -
y_train       1D array                  -
X_val         multidimensional array    -
y_val         1D array                  -
get_dict      boolean                   False
==========    ======================    =============

These are the valid keywords for algorithms:

=========    =================    ===============================================================================
algo_type    algorithm keyword    class
=========    =================    ===============================================================================
clf          all                  if the list has it at index zero then it presumes that it contains all keywords
clf          cat                  CatBoostClassifier
clf          ada                  AdaBoostClassifier
clf          dtr                  DecisionTreeClassifier
clf          raf                  RandomForestClassifier
clf          lbm                  LGBMClassifier
clf          ext                  ExtraTreeClassifier
clf          log                  LogisticRegression
clf          knn                  KNeighborsClassifier
clf          gnb                  GaussianNB
clf          rdg                  RidgeClassifier
clf          bnb                  BernoulliNB
clf          svc                  SVC
clf          per                  Perceptron
clf          mnb                  MultinomialNB
=========    =================    ===============================================================================

====================    ===========    ========    ================
Priority (in return)    Returns        Datatype    Condition
====================    ===========    ========    ================
1                       y_pred         1D array    always
2                       declaration    dict        get_dict is True
====================    ===========    ========    ================

commune_apply
_______________

It predicts the result due to the given declaration.

===========    ======================    =============
Parameters     Datatype                  Default Value
===========    ======================    =============
declaration    dict                      -
X_test         multidimensional array    -
===========    ======================    =============

.. attention::
    declaration can be obtained by using commune_create function.

====================    =======    ========    =========
Priority (in return)    Returns    Datatype    Condition
====================    =======    ========    =========
1                       y_pred     1D array    always
====================    =======    ========    =========

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

