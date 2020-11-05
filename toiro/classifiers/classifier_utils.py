import pandas as pd


def read_file(filename):
    """
    Read a csv file.

    Args:
        filename: (str): write your description
    """
    data = pd.read_csv(filename, delimiter='\t', header=None, dtype={0: str})
    return data


class EvaluationMetrics:

    def __init__(self, accuracy_score, macro_f1_score, classification_report,
                 elapsed_time=None):
        """
        Initialize the classification.

        Args:
            self: (todo): write your description
            accuracy_score: (todo): write your description
            macro_f1_score: (todo): write your description
            classification_report: (str): write your description
            elapsed_time: (int): write your description
        """
        self.metrics = {
            "accuracy_score": accuracy_score,
            "macro_f1_score": macro_f1_score,
            "classification_report": classification_report,
            "elapsed_time": elapsed_time
        }

    def __getitem__(self, key):
        """
        Get a value from the cache.

        Args:
            self: (todo): write your description
            key: (str): write your description
        """
        return self.metrics[key]

    def __str__(self):
        """
        Return a string representation of the metric.

        Args:
            self: (todo): write your description
        """
        output = []
        for k, v in self.metrics.items():
            output.append(f"{k}: {v}")
        return "\n".join(output)
