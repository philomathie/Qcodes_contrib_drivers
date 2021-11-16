from typing import Any

import numpy as np

from qcodes.instrument.parameter import Parameter
from qcodes.instrument.visa import VisaInstrument
from qcodes.utils import validators as vals


class RadiallSwitchController(VisaInstrument):
    """
    QCodes driver for the Radiall Switch Controller
    """

    def __init__(self, name: str, address: str, **kwargs: Any):
        super().__init__(name, address, **kwargs)
        
        self.visa_handle.write_termination = '\n'
        self.visa_handle.read_termination = '\r\n'

        self.add_parameter(name='channel',
                           label='Channel Selection, 1 to 6, 0 is reset',
                           unit=None,
                           set_cmd='AT\n{}',
                           get_cmd='AT\nSTATUS',
                           initial_value=0,
                           val_mapping={0:'CH_RESET',1:'CH1', 2:'CH2', 3:'CH3', 4:'CH4',5:'CH5'})

        self.connect_message()
