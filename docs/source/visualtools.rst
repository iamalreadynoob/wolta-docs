Visual Tools
===========

This part of the library is designed for computer vision applications.

get_extensions
________________

It calculates the count of each extension in given images.

==========    ========    =============
Parameters    Datatype    Default Value
==========    ========    =============
paths         list        -
==========    ========    =============

====================    =======    ==========    =========
Priority (in return)    Returns    Datatype      Condition
====================    =======    ==========    =========
1                       counts     dictionary    always
====================    =======    ==========    =========

dataset_size_same
___________________

It checks that all images in the dataset have the same shape or not.

==========    ========    =============
Parameters    Datatype    Default Value
==========    ========    =============
paths         list        -
==========    ========    =============

====================    =======    ========    =========
Priority (in return)    Returns    Datatype    Condition
====================    =======    ========    =========
1                       same       boolean     always
====================    =======    ========    =========

dataset_ratio_same
____________________

It checks that all images in the dataset have the same ratio or not.

==========    ========    =============
Parameters    Datatype    Default Value
==========    ========    =============
paths         list        -
==========    ========    =============

====================    =======    ========    =========
Priority (in return)    Returns    Datatype    Condition
====================    =======    ========    =========
1                       same       boolean     always
====================    =======    ========    =========

crop
_______

It crops the image from the centre in the requested shape.

===========    ===============================    =============
Parameters     Datatype                           Default Value
===========    ===============================    =============
img            image object (OpenCV preferred)    -
path           string                             None
crop_width     integer                            256
crop_height    integer                            256
get_img        boolean                            False
===========    ===============================    =============

.. note::
    path holds the location info for the cropped image where it will be saved. If it is None, then the image is not being saved.

====================    =======    ===================    ===============
Priority (in return)    Returns    Datatype               Condition
====================    =======    ===================    ===============
1                       img        OpenCV image object    get_img is True
====================    =======    ===================    ===============

fill
______

It fills with white the outside of the image to reach the desired shape.

===========    ===============================    =============
Parameters     Datatype                           Default Value
===========    ===============================    =============
img            image object (OpenCV preferred)    -
path           string                             None
fill_width     integer                            256
fill_height    integer                            256
get_img        boolean                            False
===========    ===============================    =============

.. note::
    path holds the location info for the cropped image where it will be saved. If it is None, then the image is not being saved.

====================    =======    ===================    ===============
Priority (in return)    Returns    Datatype               Condition
====================    =======    ===================    ===============
1                       img        OpenCV image object    get_img is True
====================    =======    ===================    ===============

make_square
____________

It follows a predetermined workflow to fit all images inside the directory to the requested square shape.

==========    ========    =============
Parameters    Datatype    Default Value
==========    ========    =============
dir_from      string      -
dir_to        string      -
edge_len      integer     256
==========    ========    =============

.. attention::
    This function does not return anything.


dir_split
__________

It splits images as train, test and split, then copies images to inner class folders. It is quite useful for image classification problems which are dealt by YOLO.

==========    ========    =============
Parameters    Datatype    Default Value
==========    ========    =============
src_dir       string      -
dest_dir      string      -
test_size     float       -
val_size      float       -
==========    ========    =============

.. note::
    directory at dest_dir might exist but it must be empty.

.. attention::
    test_size and val_size must be less than 1, bigger than 0.

.. attention::
    This function does not return anything.


cls_img_counter
_________________

It counts what class has how many images; this function is dataset organisation independent.

==========    ========    =============
Parameters    Datatype    Default Value
==========    ========    =============
dir_path      string      -
==========    ========    =============

====================    =============    ==========    =========
Priority (in return)    Returns          Datatype      Condition
====================    =============    ==========    =========
1                       class_amounts    dictionary    always
====================    =============    ==========    =========
