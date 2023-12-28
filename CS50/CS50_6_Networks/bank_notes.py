#This is a model that detects counterfeit banknotes from normal ones.

import csv
import tensorflow as tf
from sklearn.model_selection import train_test_split

with open("banknotes.csv") as f:
    reader = csv.reader(f)
    next(reader) #To enter the next line
    data = []
    for row in reader:
        data.append({
            "evidence": [float(cell) for cell in row[:4]],
            "label": 1 if row[4] == "0" else 0
        })

evidence = [row["evidence"] for row in data]
labels = [row["label"] for row in data]
X_training, X_testing, y_training, y_testing = train_test_split(
    evidence, labels, test_size=0.4
)

model = tf.keras.models.Sequential() #Sequential means multi-layered neural networks
model.add(tf.keras.layers.Dense(8, input_shape=(4,), activation="relu")) #Dense means each of the nodes is connected to other nodes. 8 Units will be inside it. 
                                                                         #Input Shape is the number of inputs
                                                                         #This Layer is hidden
                                                                    
model.add(tf.keras.layers.Dense(1, activation="sigmoid")) #Adding an output layer with 1 unit
                                                          #Sigmoid Activation
model.compile(
    optimizer="adam",
    loss="binary-crossentropy",
    metrics=["accuracy"] # How I want to accurately is my model performing.
)
#epochs specify the number of iteractions of fitting that occurs
model.fit(X_training, y_training, epochs=20)

#Evaluate is to test the model
model.evaluate(X_testing, y_testing, verbose=2)

#TensorFlow runs the backpropogation algorithm to learn what all the weights should be, by minimizing the loss
