import pandas as pd


def read_file(filename):
    data = pd.read_csv(filename, delimiter='\t', header=None, dtype={0: str})
    return data


class EvaluationMetrics:

    def __init__(self, accuracy_score, macro_f1_score, classification_report,
                 elapsed_time=None):
        self.metrics = {
            "accuracy_score": accuracy_score,
            "macro_f1_score": macro_f1_score,
            "classification_report": classification_report,
            "elapsed_time": elapsed_time
        }

    def __getitem__(self, key):
        return self.metrics[key]

    def __str__(self):
        output = []
        for k, v in self.metrics.items():
            output.append(f"{k}: {v}")
        return "\n".join(output)
