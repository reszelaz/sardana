#!/usr/bin/env python

##############################################################################
##
# This file is part of Sardana
##
# http://www.sardana-controls.org/
##
# Copyright 2011 CELLS / ALBA Synchrotron, Bellaterra, Spain
##
# Sardana is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
##
# Sardana is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
##
# You should have received a copy of the GNU Lesser General Public License
# along with Sardana.  If not, see <http://www.gnu.org/licenses/>.
##
##############################################################################

import uuid
import timeit
from unittest import TestCase

from taurus import Device
from taurus.test.base import insertTest

from sardana.pool.pooldefs import AcqSynchType
from sardana.taurus.core.tango.sardana.pool import registerExtensions
from sardana.tango.pool.test.base_sartest import SarTestTestCase


class TestPerfMeasurementGroup(SarTestTestCase):

    def setUp(self):
        SarTestTestCase.setUp(self)
        registerExtensions()

    def stress_count(self, elements, repeats, synchronizer, synchronization):
        mg_name = str(uuid.uuid1())
        argin = [mg_name] + elements
        self.pool.CreateMeasurementGroup(argin)
        try:
            mg = Device(mg_name)
            mg.setSynchronizer(synchronizer, elements[0], apply=False)
            mg.setSynchronization(synchronization, elements[0])
            total = timeit.Timer(lambda: mg.count(0.001)).timeit(repeats)
            print(total/repeats)
        finally:
            mg.cleanUp()
            self.pool.DeleteElement(mg_name)

    def tearDown(self):
        SarTestTestCase.tearDown(self)


@insertTest(helper_name="stress_count",
            test_method_doc="count with CT (software trigger)",
            elements=["_test_ct_1_1"], repeats=100,
            synchronizer="software", synchronization=AcqSynchType.Trigger)
class TestPerfMeasurementGroup_1Ctrl_1Ch(TestPerfMeasurementGroup, TestCase):
    cls_list = [
        ('CTExpChannel', 'DummyCounterTimerController',
         'DummyCounterTimerController', '_test_ct', '1', 1),
    ]
    pseudo_cls_list = []


@insertTest(helper_name="stress_count",
            test_method_doc="count with CT (software trigger)",
            elements=["_test_ct_1_1", "_test_ct_1_2", "_test_ct_1_3",
                      "_test_ct_1_4", "_test_ct_1_5"], repeats=100,
            synchronizer="software", synchronization=AcqSynchType.Trigger)
class TestPerfMeasurementGroup_1Ctrl_5Ch(TestPerfMeasurementGroup, TestCase):
    cls_list = [
        ('CTExpChannel', 'DummyCounterTimerController',
         'DummyCounterTimerController', '_test_ct', '1', 5),
    ]
    pseudo_cls_list = []


@insertTest(helper_name="stress_count",
            test_method_doc="count with CT (software trigger)",
            elements=["_test_ct_1_1", "_test_ct_1_2", "_test_ct_1_3",
                      "_test_ct_1_4", "_test_ct_1_5", "_test_ct_2_1",
                      "_test_ct_2_2", "_test_ct_2_3", "_test_ct_2_4",
                      "_test_ct_2_5"], repeats=100,
            synchronizer="software", synchronization=AcqSynchType.Trigger)
class TestPerfMeasurementGroup_2Ctrl_5Ch(TestPerfMeasurementGroup, TestCase):
    cls_list = [
        ('CTExpChannel', 'DummyCounterTimerController',
         'DummyCounterTimerController', '_test_ct', '1', 5),
        ('CTExpChannel', 'DummyCounterTimerController',
         'DummyCounterTimerController', '_test_ct', '2', 5),
    ]
    pseudo_cls_list = []


@insertTest(helper_name="stress_count",
            test_method_doc="count with CT (software trigger)",
            elements=["_test_ct_1_1", "_test_ct_1_2", "_test_ct_1_3",
                      "_test_ct_1_4", "_test_ct_1_5", "_test_ct_2_1",
                      "_test_ct_2_2", "_test_ct_2_3", "_test_ct_2_4",
                      "_test_ct_2_5", "_test_ct_3_1", "_test_ct_3_2",
                      "_test_ct_3_3", "_test_ct_3_4", "_test_ct_3_5",
                      "_test_ct_4_1", "_test_ct_4_2", "_test_ct_4_3",
                      "_test_ct_4_4", "_test_ct_4_5"],
                      repeats=100,
            synchronizer="software", synchronization=AcqSynchType.Trigger)
class TestPerfMeasurementGroup_4Ctrl_5Ch(TestPerfMeasurementGroup, TestCase):
    cls_list = [
        ('CTExpChannel', 'DummyCounterTimerController',
         'DummyCounterTimerController', '_test_ct', '1', 5),
        ('CTExpChannel', 'DummyCounterTimerController',
         'DummyCounterTimerController', '_test_ct', '2', 5),
        ('CTExpChannel', 'DummyCounterTimerController',
         'DummyCounterTimerController', '_test_ct', '3', 5),
        ('CTExpChannel', 'DummyCounterTimerController',
         'DummyCounterTimerController', '_test_ct', '4', 5),
    ]
    pseudo_cls_list = []


@insertTest(helper_name="stress_count",
            test_method_doc="count with CT (software trigger)",
            elements=["_test_ct_1_1", "_test_ct_1_2", "_test_ct_1_3",
                      "_test_ct_1_4", "_test_ct_1_5","_test_ct_1_6",
                      "_test_ct_1_7", "_test_ct_1_8", "_test_ct_1_9",
                      "_test_ct_1_10",
                      "_test_ct_2_1", "_test_ct_2_2", "_test_ct_2_3",
                      "_test_ct_2_4", "_test_ct_2_5", "_test_ct_2_6",
                      "_test_ct_2_7", "_test_ct_2_8", "_test_ct_2_9",
                      "_test_ct_2_10"],
                      repeats=100,
            synchronizer="software", synchronization=AcqSynchType.Trigger)
class TestPerfMeasurementGroup_2Ctrl_10Ch(TestPerfMeasurementGroup, TestCase):
    cls_list = [
        ('CTExpChannel', 'DummyCounterTimerController',
         'DummyCounterTimerController', '_test_ct', '1', 10),
        ('CTExpChannel', 'DummyCounterTimerController',
         'DummyCounterTimerController', '_test_ct', '2', 10),
    ]
    pseudo_cls_list = []