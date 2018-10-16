# Class for loading and preprocessing a dataset.

from pathlib import Path
from lib.TextPreprocessor import TextPreprocessor
import pandas as pd


class ETL:

    def __init__(self, dpath_raw, dpath_tokenised, dpath_redux_bow):
        # paths
        self.dpath_raw = dpath_raw
        self.dpath_tokenised = dpath_tokenised
        self.dpath_redux_bow = dpath_redux_bow

        # datasets
        self.data_raw = None
        self.data_tokenised = None

        # meta data
        self.comment_lengths = []

    def __load_data(self, dpath):
        """

        :param dpath:
        :return:
        """
        return pd.read_csv(dpath, index_col=False)

    def get_tokenised_data(self):
        """

        :return:
        """
        tp = TextPreprocessor()

        preprocessed_file = Path(self.dpath_tokenised)
        if not preprocessed_file.is_file():
            print("Preprocessing and saving data")
            self.data_raw = self.__load_data(self.dpath_raw)
            tokenised_comments, self.comment_lengths = tp.tokenise(self.data_raw['comment_text'])

            # # TODO: preallocate
            # tokenised_comments_padded = []
            # for tc in tokenised_comments:
            #     tokenised_comments_padded.append(tc + ['_pad_'] * (max(comment_lengths) - len(tc)))
            # print(tokenised_comments_padded[0])
            # tokenised_comments = tokenised_comments_padded

            self.data_tokenised = pd.DataFrame(tokenised_comments)
            self.data_tokenised.to_csv(self.dpath_tokenised, index=False, header=False)
        else:
            print("Loading preprocessed data")

            # Import preprocessed data
            self.data_tokenised = pd.read_csv(preprocessed_file, index_col=False)

            for _, v in self.data_tokenised.iterrows():
                self.comment_lengths.append(len(v))

    def get_reduced_bow_input(self):
        """

        :return:
        """
        tp = TextPreprocessor()

        print("Preprocessing and saving data")
        self.data_raw = self.__load_data(self.dpath_raw)
        num_of_comments = len(self.data_raw)

        newCol = []

        for i, v in self.data_raw.iterrows():
            if i % 1000 == 0:
                print("comment {} of {}".format(i, num_of_comments))
            # self.data_raw.iloc[i]["comment_text"] =
            newCol.append(tp.clean_string(v["comment_text"]))

        # Replace all text with processed text.
        self.data_raw.drop("comment_text", axis=1, inplace=True)

        # Put whatever series you want in its place
        self.data_raw["comment_text"] = newCol

        print("writing with header {}".format(self.data_raw.columns))
        self.data_raw.to_csv(self.dpath_redux_bow, index=False, header=self.data_raw.columns)
