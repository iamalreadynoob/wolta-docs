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