# TNeGA_internship
Works and codes

#About waitKey and mask number 
First, cv2.waitKey(1) & 0xFF will be executed.

Doing wait 1 ms for user press.
If user press, for example, q then waitKey return DECIMAL VALUE of q is 113. In Binary, It is expressed as 0b01110001.
Next, AND operator is excuted with two inputs are 0b01110001 and 0xFF (0b11111111).
0b01110001 AND 0b11111111 = 0b01110001. Exactly result is DECIMAL VALUE of q

Second, compare value of left expression 0b01110001 with ord('q'). Clearly, these values is the same as another value. And final result is break is invoked.
