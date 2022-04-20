import json
import pandas as pd


def compare_models(correct_model, input_model):
    """
    Compare two models and return a similarity score
    """

    # sort the models
    correct_model_sorted = sorted(
        correct_model, key=lambda x: (x['x'], x['y'], x['z']))
    input_model_sorted = sorted(
        input_model, key=lambda x: (x['x'], x['y'], x['z']))

    # Convert the models to pandas dataframes
    correct_model_df = pd.DataFrame(correct_model_sorted)
    input_model_df = pd.DataFrame(input_model_sorted)

    score = 0

    # loop through the columns, and find the input coordinates that matches the correct coordinates
    for i in range(len(input_model_df)):
        key = input_model_df.iloc[i]

        find_data = correct_model_df[(correct_model_df['x'] == key.x) & (
            correct_model_df['y'] == key.y) & (correct_model_df['z'] == key.z)].head(1)

        # drop the found coordinate to avoid duplicates
        correct_model_df.drop(find_data.index, inplace=True)

        score += 1  # increment the score

    ratio = score / (len(correct_model))

    # convert to percentage and round to 3 decimal places
    similarity_score = round((ratio * 100), 3)

    print("Similarity Score: {} %".format(similarity_score))


# load the correct model
correct_model = json.loads(open('models/correct_model.json').read())

# load the input model
input_model = json.loads(open('models/model3.json').read())

compare_models(correct_model, input_model)
