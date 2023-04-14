from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, f1_score, recall_score

def evaluate_model(model, X_test, y_test):
    '''Predicts and displays the evaluation scores of the model'''
    
    predictions = model.predict(X_test)
    
    accuracy = accuracy_score(y_test, predictions)
    precision = precision_score(y_test, predictions)
    recall = recall_score(y_test, predictions)
    f1 = f1_score(y_test, predictions)
    tn, fp, fn, tp = confusion_matrix(y_test, predictions).ravel()
    
    print('Accuracy Score   ', accuracy)
    print('Precision score  ', precision)
    print('Recall score     ', recall)
    print('f1 score         ', f1)
    print('True Negatives  ', tn)
    print('False positives  ', fp)
    print('False negatives  ', fn)
    print('True positives   ', tp)
    
    
    return accuracy, precision, recall, f1, tn, fp, fn, tp