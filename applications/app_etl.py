# Application for loading, preprocessing and storing raw data.

import seaborn as sns

from lib.ToxicInvestigate import ToxicInvestigate
from lib.ETL import ETL

if __name__ == "__main__":
    sns.set(color_codes=True)

    ti = ToxicInvestigate()
    etl = ETL(dpath_raw="../data/train.csv",
              dpath_tokenised="../data/data_tokenised.csv",
              dpath_redux_bow="../data/train_red_bow.csv")

    # ti.class_balance(train_data)
    print("------- LOADING DATA -------")
    # etl.get_tokenised_data()

    # figure(figsize=(18, 7))
    # title("Comment token lengths. {} comments".format(len(comment_lengths)))
    # sns.distplot(comment_lengths)
    # show()

    # ti.show_frequent_words(etl.data_tokenised)

    etl.get_reduced_bow_input()

    # test_etl = ETL(dpath_raw="../data/test.csv",
    #                dpath_tokenised="../data/data_tokenised.csv",
    #                dpath_redux_bow="../data/test_red_bow.csv")
    #
    # test_etl.get_reduced_bow_input()

