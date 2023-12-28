import csv
import sys

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

TEST_SIZE = 0.4


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python shopping.py data")

    # Load data from spreadsheet and split into train and test sets
    evidence, labels = load_data(sys.argv[1])
    X_train, X_test, y_train, y_test = train_test_split(
        evidence, labels, test_size=TEST_SIZE
    )

    # Train model and make predictions
    model = train_model(X_train, y_train)
    predictions = model.predict(X_test)
    sensitivity, specificity = evaluate(y_test, predictions)

    # Print results
    print(f"Correct: {(y_test == predictions).sum()}")
    print(f"Incorrect: {(y_test != predictions).sum()}")
    print(f"True Positive Rate: {100 * sensitivity:.2f}%")
    print(f"True Negative Rate: {100 * specificity:.2f}%")


def load_data(filename):
    """
    Load shopping data from a CSV file `filename` and convert into a list of
    evidence lists and a list of labels. Return a tuple (evidence, labels).

    evidence should be a list of lists, where each list contains the
    following values, in order:
        - Administrative, an integer
        - Administrative_Duration, a floating point number
        - Informational, an integer
        - Informational_Duration, a floating point number
        - ProductRelated, an integer
        - ProductRelated_Duration, a floating point number
        - BounceRates, a floating point number
        - ExitRates, a floating point number
        - PageValues, a floating point number
        - SpecialDay, a floating point number
        - Month, an index from 0 (January) to 11 (December)
        - OperatingSystems, an integer
        - Browser, an integer
        - Region, an integer
        - TrafficType, an integer
        - VisitorType, an integer 0 (not returning) or 1 (returning)
        - Weekend, an integer 0 (if false) or 1 (if true)

    labels should be the corresponding list of labels, where each label
    is 1 if Revenue is true, and 0 otherwise.
    """
    evidence = []
    labels = []
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        firstRow = True
        for row in csvreader:
            if firstRow == True:
                firstRow = False
                continue
            month = {"Jan":0,"Feb":1,"Mar":2, "Apr":3, "May":4, "June":5, "Jul":6, "Aug":7, "Sep":8, "Oct":9, "Nov":10, "Dec":11}
            visitorType = {"Returning_Visitor":1, "New_Visitor":0,"Other":2}
            weekend = {"FALSE":0, "TRUE":1}
            label = {"FALSE":0, "TRUE":1}
            evidence.append([int(row[0]),float(row[1]), int(row[2]), float(row[3]), int(row[4]), float(row[5]), float(row[6]), float(row[7]), float(row[8]), float(row[9]), month[row[10]], int(row[11]), int(row[12]), int(row[13]), int(row[14]), visitorType[row[15]],  weekend[row[16]]])
            labels.append(label[row[17]])
    return (evidence, labels)

def train_model(evidence, labels):
    """
    Given a list of evidence lists and a list of labels, return a
    fitted k-nearest neighbor model (k=1) trained on the data.
    """
    neigh = KNeighborsClassifier(1)
    neigh.fit(evidence,labels)
    return neigh

def evaluate(labels, predictions):
    """
    Given a list of actual labels and a list of predicted labels,
    return a tuple (sensitivity, specificity).

    Assume each label is either a 1 (positive) or 0 (negative).

    `sensitivity` should be a floating-point value from 0 to 1
    representing the "true positive rate": the proportion of
    actual positive labels that were accurately identified.

    `specificity` should be a floating-point value from 0 to 1
    representing the "true negative rate": the proportion of
    actual negative labels that were accurately identified.
    """
    countp = 0
    countn = 0
    countpprediction = 0
    countnprediction = 0
    for (label,prediction) in zip(labels,predictions):
        if(label == 1):
            countp += 1
        else:
            countn += 1
        if(label == prediction == 1):
            countpprediction += 1
        elif(label == prediction == 0):
            countnprediction += 1
            
    print(countpprediction/countp)
    print(countnprediction/countn)
    return (countpprediction/countp,countnprediction/countn)

if __name__ == "__main__":
    main()
