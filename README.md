UDP Chat Room
-----------------------------
* How to Download the Programs
    * Downloading chat.py & server.py
* How To Run the Programs
    * Running server.py
        - cd into the directory where you downloaded the files
        - Run `python server.py`
    * Running chat.py
        - cd into the directory where you downloaded the files
        - Run `python chat.py`
        - Run this in multiple terminals if you want to have multiple clients

* TODO:
    * implement go-back-n with sequence numbers/acknowledgements
    * acknowledgement = sequence number + length of packet in bytes (seq number 123 of a 80 byte packet = ack203)
    * implement seq/ack on file transfer for reliable file transfer
