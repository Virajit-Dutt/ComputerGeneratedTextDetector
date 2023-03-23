def predict(text):
    import pickle
    import os

    print('\n\n\n')
    print(os.getcwd())
    print()

    model = pickle.load(open('models/model.pkl', 'rb'))
    vectorizer = pickle.load(open('models/transform.pkl', 'rb'))

    text = vectorizer.transform([text])
    prediction = model.predict(text)

    return prediction[0]