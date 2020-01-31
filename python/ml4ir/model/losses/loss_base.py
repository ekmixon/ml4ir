from ml4ir.config.keys import LossTypeKey

from typing import Optional, Union


class RankingLossBase(object):

    loss_type: Optional[str] = None

    def __init__(self, loss_key, scoring_key):
        self.loss_key = loss_key
        self.scoring_key = scoring_key

    def get_loss_fn(self, **kwargs):
        """
        Returns the loss function _loss_fn()
        """
        return self._make_loss_fn(**kwargs)

    def _make_loss_fn(self, **kwargs):
        """
        Define a ranking loss function with necessary custom methods

        NOTE: Should consider different types of scoring functions
        """

        def _loss_fn(y_true, y_pred):
            pass

        return _loss_fn


class PointwiseLossBase(RankingLossBase):

    loss_type = LossTypeKey.POINTWISE


class PairwiseLossBase(RankingLossBase):

    loss_type = LossTypeKey.PAIRWISE


class ListwiseLossBase(RankingLossBase):

    loss_type = LossTypeKey.LISTWISE
