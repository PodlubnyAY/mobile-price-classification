import logging
import pandas as pd
import pickle as pkl

logger = logging.getLogger("api_handler")
class FastAPIHandler():

    def __init__(self):
        try:
            with open('../models/model.pkl', 'rb') as f:
                self.model = pkl.load(f)
            logger.info('Model is loaded')
        except Exception as e:
            logger.error(f'Error loading model: {e}')

    def predict(self, item_features:dict):
        item_df = pd.DataFrame(data=item_features, index=[0])
        prediction = self.model.predict(item_df)
        return prediction