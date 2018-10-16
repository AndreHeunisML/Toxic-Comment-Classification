

import pandas as pd


class ToxicInvestigate:

    def class_balance(self, inp_df):
        """

        :param inp_df:
        :return:
        """
        # full_len = len(train_data)
        # print("full length", full_len)
        #
        # tox_len = len(train_data[train_data["toxic"] == 1])
        # print("toxic length: {} {}".format(tox_len, tox_len / float(full_len)))
        #
        # severe_tox_len = len(train_data[train_data["severe_toxic"] == 1])
        # print("severe toxic length: {} {}".format(severe_tox_len,  severe_tox_len / float(full_len)))
        #
        # obscene_len = len(train_data[train_data["obscene"] == 1])
        # print("obscene length: {} {}".format(obscene_len, obscene_len / float(full_len)))
        #
        # threat_len = len(train_data[train_data["threat"] == 1])
        # print("threat length: {} {}".format(threat_len, threat_len / float(full_len)))
        #
        # insult_len = len(train_data[train_data["insult"] == 1])
        # print("insult length: {} {}".format(insult_len, insult_len / float(full_len)))
        #
        # identity_hate_len = len(train_data[train_data["identity_hate"] == 1])
        # print("identity_hate length: {} {}".format(identity_hate_len,  identity_hate_len / float(full_len)))
        # print()
        # print(train_data["comment_text"].head(n=20))
        print(inp_df["comment_text"].values)
        print(type(inp_df["comment_text"].values))
        print(type(inp_df["comment_text"].values[0]))
        print(len(inp_df["comment_text"].values))

        # comments = train_data["comment_text"]
        #
        # for i, v in comments.iteritems():
        #     print("------------------")
        #     print(v)

        # labels = train_data['label'].values
        # train_data = train_data.drop('label', axis=1).values

    def show_frequent_words(self, tokenised_data):
        """

        :return:
        """
        print("Storing word frequencies")
        word_counts = pd.Series(tokenised_data.values.flatten()).value_counts()
        print("Unique words: {}".format(len(word_counts)))

        word_counts.to_csv('../data/data_wf.csv')


