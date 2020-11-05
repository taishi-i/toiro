from .classifier_utils import (
    read_file,
    EvaluationMetrics
)

from .classifier_svm import SVMClassificationModel


try:
    import torch
    import transformers
    import catalyst
    _bert_available = True
except:
    _bert_available = False


def is_bert_available():
    """
    Return true if all available sanity is available.

    Args:
    """
    return _bert_available


if is_bert_available():
    from .classifier_bert import BERTClassificationModel
