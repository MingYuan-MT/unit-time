#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
from .CTC_ import CTC  # 农历转阳历
from .LSC import LunarDate, SolarDate, LunarSolarDateConverter  # 阴历和阳历转换
from .SC_ import SC  # 阳历转农历
from .batchcalendar import BatchCalendar  # 批量转换日历

__version__ = '2021.8.7'
__author__ = 'Jader'
__description__ = '常见的日历转换器'
__email__ = 'hmy940118@gmail.com'
__names__ = 'unit-calendar'
__url__ = 'https://github.com/Jader'
