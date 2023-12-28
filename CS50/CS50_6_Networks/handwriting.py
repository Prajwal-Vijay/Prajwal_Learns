import sys
import tensorflow as tf
mnist = tf.keras.datasets.mnist #This is a famous dataset of people's handwritten digits.

#All this to get the data into a nice usable form.
(x_train, y_train) ,(x_test,y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0 #as color values range from 0 to 255
y_train = tf.keras.utils.to_categorically(y_train)
y_test = tf.keras.utils.to_categorically(y_test)
x_train = x_train.reshape(
    x_train.shape[0], x_train.shape[1], x_train.shape[2], 1
)
x_test = x_test.reshape(
    x_test.shape[0], x_test.shape[1], x_test.shape[2], 1
)
#Creates the Neural Network, instead of using add layer to add layers again and again, we can simply pass the list to be added as parameters
model = tf.keras.models.Sequential([
    
    #This is the convolutional layer, where we learn 32 layers.
    tf.keras.layers.Conv2D(
        32, (3,3), activation="relu", input_shape=(28,28,1) #3x3 matrix is used, activation function is relu, The MNIST dataset has 28x28 pictures, 
                                                            #1 refers to number of color channels, which is 1 for black/white, for colored it is 3 (r,g,b)
                                                            #32 refers to the number of filters that will be created
    ),
    
    #Max-pooling Layer [to minimize the inputs]
    tf.keras.layers.MaxPooling2D(pool_size=(2,2)),
    
    #Flattening all the units into inputs
    tf.keras.layers.Flatten(),
    
    #Adding Hidden Layers with dropout
    tf.keras.layers.Dense(128,activation="relu"),
    tf.keras.layers.Dropout(0.5), #While training it will prevent overfitting
    
    tf.keras.layers.Dense(10,activation="softmax")
])

model.compile(
    optimizer="adam",
    loss="categorical_crossentropy",
    metrics=["accuracy"]
)
model.fit(x_train,y_train,epochs=10)
model.evaluate(x_test,y_test, verbose=2)

#Tensor Flow allows us to save the model [the weights] to a file
if len(sys.argv) == 2:
    filename = sys.argv[1]
    model.save(filename)
    print(f"Model Saved to {filename}.")
