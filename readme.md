This code is to be used in conjunction with Caffe code at https://github.com/BVLC/caffe @commit:de6d444445261fc9859143bfd969d538ae7a2108


Change the path to train.h5 and test.h5 in hdf5-data/train.txt and hdf5-data/test.txt 
Here is the architecure:
*The reshape layers are added sothat:
	*Reshape1 keeps the different Bounding Box values isolated during inner product.(Else ip layer will just string all these up into 1 long vector)
	*Reshape2 sothat maxpooling happens over all BBs.
*Slicelayer slices the layer into 1)layer with the softmax of IDK class and 2)layer with softmax of class1,2. This is imitating dropping IDK


                   SigmoidCrossEntropy
                        /        \
                       /          \
       (1,1,1,2)(maxpool)         (labels)
                      /              \
                   MaxPool            \
                     /                 \
       (1,1,10,2)(reshape2)             \
                    /                    \
                reshape                   \
                     \                     \ 
(10,1,1,1)(slice2) (slice1)(10,1,1,2)       \
               \     /                       \
                 slice                       |
                  /                          |
      (10,1,1,3)(softMax)                    |
                   \                         |
                  softmax                    |
                     \                       | 
           (10,1,1,3)(ip)                    |
                      \                      |
                     InnerProduct Layer     /
                        \                  /
             (10,1,1,3)(reshape1)         / 
                          \              /
                       Reshape Layer    /
                           \           /
               (1,10,1,3) (data)      / 
                             \       /
                          -------------
                         | Data Layer  |
                          -------------
