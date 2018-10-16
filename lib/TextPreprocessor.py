

import nltk
import numpy as np
import re


class TextPreprocessor:

    def clean_string(self, text):
        """

        :param string:  String to be cleaned.
        :return:        Cleaned string.
        """
        text = re.sub(r'\\n', ' ', text)

        # replace characters that repeat more than twice with one character.
        text = re.sub(r'([0-9a-zA-Z?!&*$@])\1{2,}', r'\1', text)

        # Remove unwanted characters and frequent words.
        text = re.sub(r'\b(?i)the(?i)\b|\b(?i)to(?i)\b|\b(?i)of(?i)\b|\b(?i)and(?i)\b|\b(?i)a(?i)\b', '', text)
        text = re.sub(r'\b(?i)is(?i)\b|\b(?i)that(?i)\b', '', text)
        text = re.sub(r'\b(?i)in(?i)\b|\b(?i)it(?i)\b|\b(?i)for(?i)\b|\b(?i)not(?i)\b|\b(?i)on(?i)\b', '', text)
        text = re.sub(r'\b(?i)be(?i)\b|\b(?i)this(?i)\b', '', text)
        text = re.sub(r'[^0-9a-zA-Z\d\s?!&*$@:;)(]', '', text)

        # replace very long words
        text = re.sub(r'\b[$!a-zA-Z0-9&*@_]{20,}\b', '', text)

        # transform everything to lowercase.
        text = text.lower()

        # replace any number with a number identifier.
        text = re.sub(r'\d{1,}', ' _ID-NUM_ ', text)

        # remove www.
        text = re.sub(r'\b([www])(\w +)\b', '', text)

        # remove http.
        text = re.sub(r'\b([http])(\w +)\b', '', text)

        text = re.sub(r'&lt;3', " good ", text)
        text = re.sub(r':d', " good ", text)
        text = re.sub(r':dd', " good ", text)
        text = re.sub(r':p', " good ", text)
        text = re.sub(r'8\)', " good ", text)
        text = re.sub(r':\)', " good ", text)
        text = re.sub(r';\)', " good ", text)
        text = re.sub(r'\(:', " good ", text)

        text = re.sub(r'yay!', " good ", text)
        text = re.sub(r'yay', " good ", text)
        text = re.sub(r'yaay', " good ", text)
        text = re.sub(r'yaaay', " good ", text)

        text = re.sub(r'yaaaay', " good ", text)
        text = re.sub(r'yaaaaay', " good ", text)

        text = re.sub(r':/', " bad ", text)
        text = re.sub(r':\(', " bad ", text)
        text = re.sub(r':s', " bad ", text)

        text = re.sub(r':s', " bad ", text)
        text = re.sub(r':s', " bad ", text)
        text = re.sub(r':s', " bad ", text)
        text = re.sub(r':s', " bad ", text)

        text = re.sub(r'\br\b', "are", text)
        text = re.sub(r'\bu\b', "you", text)
        text = re.sub(r'\bhaha\b', "ha", text)
        text = re.sub(r'\bhahaha\b', "ha", text)
        text = re.sub(r'\bdont\b', "do not", text)
        text = re.sub(r'\bdoesnt\b', "does not", text)
        text = re.sub(r'\bdidnt\b', "did not", text)
        text = re.sub(r'\bhasnt\b', "has not", text)
        text = re.sub(r'\bhavent\b', "have not", text)
        text = re.sub(r'\bhadnt\b', "had not", text)
        text = re.sub(r'\bwont\b', "will not", text)
        text = re.sub(r'\bwouldnt\b', "would not", text)
        text = re.sub(r'\bcant\b', "can not", text)
        text = re.sub(r'\bcannot\b', "can not", text)
        text = re.sub(r'\bim\b', "i am", text)
        text = re.sub(r'\bm\b', "am", text)
        text = re.sub(r'\bwouldnt\b', "would not", text)
        text = re.sub(r'\bill\b', "i will", text)
        text = re.sub(r'\bits\b', "it is", text)
        text = re.sub(r'\bthats\b', "that is", text)
        text = re.sub(r'\bwerent\b', "were not", text)
        text = re.sub(r'\bunneccessary\b', "unnecessary", text)
        text = re.sub(r'\bunnecesary\b', "unnecessary", text)
        text = re.sub(r'\bunecessary\b', "unnecessary", text)
        text = re.sub(r'\bunneccesary\b', "unnecessary", text)
        text = re.sub(r'\bturkeyfuck\b', "turkey fuck", text)
        text = re.sub(r'\bnigers\b', "niggers", text)
        text = re.sub(r'\bnigga\b', "nigger", text)
        text = re.sub(r'\bniggerjew\b', "nigger jew", text)
        text = re.sub(r'\bniggors\b', "niggers", text)
        text = re.sub(r'\bniggaz\b', "niggers", text)
        text = re.sub(r'\bnein\b', "no", text)
        text = re.sub(r'\btitties\b', "tits", text)
        text = re.sub(r'\btho\b', "though", text)
        text = re.sub(r'\bthankyou\b', "thankyou", text)
        text = re.sub(r'\bsucksgeorge\b', "sucks", text)
        text = re.sub(r'\bsuckernguyen\b', "sucker", text)
        text = re.sub(r'\bsuckernguyen\b', "sucker", text)
        text = re.sub(r'\bshitfuck\b', "shit fuck", text)
        text = re.sub(r'\bshithead\b', "shit head", text)
        text = re.sub(r'\bshithole\b', "shit hole", text)
        text = re.sub(r'\banalanal\b', "anal", text)

        # replace any single characters left over.
        text = re.sub(r'\b[a-zA-Z]\b', '', text)

        return text

    def tokenise(self, strings):
        """

        :param strings: 1D numpy array of strings
        :return:
        """
        print("tokenising comments...")
        tokenised_strings = []
        num_of_comments = len(strings)

        comment_lengths = []

        for i, text in enumerate(strings):
            if i % 1000 == 0:
                print("comment {} of {}".format(i, num_of_comments))

            text = self.clean_string(text)

            # Split into tokens
            token_string = nltk.word_tokenize(text)

            # If the same token appears many times, just keep the first instance.
            if len(token_string) > 100:
                token_string = np.array(token_string)
                wordset = set(token_string)

                inds = dict()
                ind_remove = []
                for word in wordset:
                    inds[word] = np.where(token_string == word)[0]

                    if len(inds[word]) > 10:
                        ind_remove.extend(inds[word][1:])

                token_string = np.delete(token_string, ind_remove).tolist()

            # Skip super long comments
            if len(token_string) > 1000:
                print(token_string)
                continue

            # Store
            comment_lengths.append(len(token_string))
            tokenised_strings.append(token_string)

        print("Maximum token length is {}".format(max(comment_lengths)))

        return tokenised_strings, comment_lengths

