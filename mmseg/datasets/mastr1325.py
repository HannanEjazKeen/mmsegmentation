from mmseg.registry import DATASETS
from .basesegdataset import BaseSegDataset

@DATASETS.register_module()

class Mastr1325Dataset(BaseSegDataset):

    METAINFO = dict(
            classes=('environment','water','sky','unreserved','unknown'),
            palatte=[[255,0,0],[0,255,0],[0,0,255],[0,0,0],[255,255,255]])

    def __init__(self, **kwargs):
        super(Mastr1325Dataset, self).__init__(
            img_suffix='.jpg', seg_map_suffix='.png', **kwargs)
