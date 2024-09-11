Further Readings
==================

.. _transformation:

Transformations
________________

The transformation process can be used to achieve normal distribution behaviour in a set that does not show it naturally. These ways are supported by the Wolta library:

=======    ==============    ============
name       core operation    calculation
=======    ==============    ============
log        natural log       ln(A)
log-m      natural log       ln(A + m)
log2       base 2 log        log_2(A)
log2-m     base 2 log        log_2(A + m)
log10      common log        log(A)
log10-m    common log        log(A + m)
sqrt       square root       A^0.5
sqrt-m     square root       (A + m)^0.5
cbrt       cube root         A^(1/3)
=======    ==============    ============

.. attention::
    'A' stands for a set, m stands for the smallest member of the set A.

.. note::
    This process is reversible.

.. _distribution:

Categorization With Normal Distribution
_________________________________________

If the set has a normal distribution, it can be split into three groups. In order to do that min, max, standard deviation and arithmetic mean should be calculated.

=====    ===========================
class    interval
=====    ===========================
0        min <= y <= mean - std
1        mean - std < y < mean + std
2        mean + std <= y <= max
=====    ===========================


.. _welkin:

Welkin Classification
________________________

Welkin classification is designed for prediction on datasets that have discrete value distributions in features for each class. It determines the intervals in every feature for each class independently by calculating the minimum and maximum values.

.. attention::
    In the prediction phase, it may search the most fitted class for a test sample (strategy='travel') or when a class has enough coherence, it can be accepted directly as a prediction (strategy='limit'). Limit strategy is less time consuming than travel strategy.

.. attention::
    Also, there is no need to use all the features for training and predicting, only requested features can be used thanks to the priority parameter.

.. _dist:

Dist Regression
________________________

Dist Regressor comes up with the idea that the sets with smaller ranges may cause more accurate predictions for regression algorithms. If the output set has a normal distribution then the algorithm splits it into three classes (for more information about it read :ref:`distribution` article) and then trains regression models individually. After that, in the prediction phase, first it uses classification and detects the class then what regression algorithm will be used and finally according to that makes a prediction.

.. note::
    By using random under sampler, classes can be balanced for classification.

.. _commune:

Classification with Commune Technique
________________________

This technique follows these steps:

1. Train the models.
2. Find the algorithm that gives the best accuracy score for the dataset. It is called a 'general model'.
3. Find the algorithm that gives the best accuracy score for each class independently. Each one of them is called a 'submodel.''
4. Collect the samples from the validation set that do not have the same result in general and submodel. Predict them again with all algorithms and find the best result given one. It is called an 'instead model' and it is used in situations like this in the prediction phase.
