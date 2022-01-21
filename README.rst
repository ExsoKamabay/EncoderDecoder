``KAMABAY`` ENCODE DECODE 
--------------------------

encode your data decode, KAMABAY ``encode decode based`` on ``dictionary``  you can change its output encode value by changing the value in its dictionary.



**Installation**

.. code :: python

        #requires python3
        pip install kamabayEncoder
        """


``URL`` `https://pypi.org/project/kamabayEncoder/`_

Simple Example
----------------
.. code :: python

        >>> from kamabayEncoder import KAMABAY_ENCODE_DECODE
        >>>
        >>> start = KAMABAY_ENCODE_DECODE(data="hallo guys!",save=False)
        >>> start.encode()
        '$dsew[KMY]!@$#%[KMY]me&yu[KMY]me&yu[KMY]p039=[KMY]4%32[KMY]ifaqd[KMY]po;pd[KMY]u`u!y[KMY]edwqe[KMY]$4asq[KMY]'
        >>> start.decode()
        "KeyError 'hallo guys!'"
        >>>
        >>> data = "$dsew[KMY]!@$#%[KMY]me&yu[KMY]me&yu[KMY]p039=[KMY]4%32[KMY]ifaqd[KMY]po;pd[KMY]u`u!y[KMY]edwqe[KMY]$4asq[KMY]"
        >>> start = KAMABAY_ENCODE_DECODE(data=data,save=False)
        >>> start.encode()
        TypeError('$dsew[KMY]!@$#%[KMY]me&yu[KMY]me&yu[KMY]p039=[KMY]4%32[KMY]ifaqd[KMY]po;pd[KMY]u`u!y[KMY]edwqe[KMY]$4asq[KMY]')
        >>> start.decode()
        'hallo guys!'
        >>>


Encode
--------
.. code :: python
        
        from kamabayEncoder import KAMABAY_ENCODE_DECODE
        
        data = "hello world"# type data string
        save = True         # type boolean save file output data.kmy
        kamabay = KAMABAY_ENCODE_DECODE(
            data = data,
            save = save);
        print(kamabay.encode());

**output** >  ``$dsew[KMY]fgdgf[KMY]me&yu[KMY]me&yu[KMY]p039=[KMY]4%32[KMY]^'-hd[KMY]p039=[KMY]3sdfh[KMY]me&yu[KMY]~gd!2[KMY]``

Decode
--------
.. code :: python
        
        from kamabayEncoder import KAMABAY_ENCODE_DECODE
        
        data = "$dsew[KMY]fgdgf[KMY]me&yu[KMY]me&yu[KMY]p039=[KMY]4%32[KMY]^'-hd[KMY]p039=[KMY]3sdfh[KMY]me&yu[KMY]~gd!2[KMY]"
        save = False 
        kamabay = KAMABAY_ENCODE_DECODE(
            data = data,
            save = save);
        print(kamabay.decode());
        
**output** > ``hello world``

Show dictionary
----------------
.. code :: python
        
        from kamabayEncoder import KAMABAY_ENCODE_DECODE
        
        dictionary = KAMABAY_ENCODE_DECODE(
                        data="NONE",
                        save=False);
        
        print(dictionary.showDict(auth="KAMABAY"))
        # hasil menampilkan kamus 

**output displays the json dictionary!**



``@copyright 21052021``

``mail`` `lexyong66@gmail.com`_ 

.. _lexyong66@gmail.com : lexyong66@gmail.com
.. _https://pypi.org/project/kamabayEncoder/ : https://pypi.org/project/kamabayEncoder/
