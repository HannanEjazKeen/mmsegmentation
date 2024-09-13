from mmseg.registry import DATASETS
from .basesegdataset import BaseSegDataset

@DATASETS.register_module()

class AerialFluvialDataset(BaseSegDataset):

    METAINFO = dict(
            classes=('environment','water'),
            palatte=[[255,0,0],[0,255,0]])

    def __init__(self, **kwargs):
        super(AerialFluvialDataset, self).__init__(
            img_suffix='.jpg', seg_map_suffix='.png', **kwargs)
