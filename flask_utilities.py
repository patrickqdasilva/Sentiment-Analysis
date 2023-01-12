import pickle
MODEL_PATH = r'C:\Users\Patrick\Desktop\Flask App Sentiment Analyis\cv_nb_pipe.pkl'

# Load the model
with open(MODEL_PATH, 'rb') as f:
    model = pickle.load(f)

# Define a helper function for preprocessing the input text
def remove_non_letters(text):
    # Use a regular expression to match all non-letter characters (and spaces)
    import re
    pattern = re.compile(r'[^a-zA-Z\s]')
    return pattern.sub('', text)

# Define a helper function for postprocessing the prediction
def postprocess(prediction):
    if prediction == 0:
        return 'Negative'
    elif prediction == 1:
        return 'Neutral'
    elif prediction == 2:
        return 'Positive'
    else:
        return 'Error'

# Final Pipeline that combines preprocessing steps and prediction
def make_prediction(text):
    text = remove_non_letters(text)
    prediction = model.predict([text])
    return postprocess(prediction)