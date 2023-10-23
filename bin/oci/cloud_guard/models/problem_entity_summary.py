# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ProblemEntitySummary(object):
    """
    The information about problem entities details of DataSource for a CloudGuard Problem.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ProblemEntitySummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param regions:
            The value to assign to the regions property of this ProblemEntitySummary.
        :type regions: list[str]

        :param time_first_detected:
            The value to assign to the time_first_detected property of this ProblemEntitySummary.
        :type time_first_detected: datetime

        :param problem_id:
            The value to assign to the problem_id property of this ProblemEntitySummary.
        :type problem_id: str

        :param time_last_detected:
            The value to assign to the time_last_detected property of this ProblemEntitySummary.
        :type time_last_detected: datetime

        :param result_url:
            The value to assign to the result_url property of this ProblemEntitySummary.
        :type result_url: str

        :param entity_details:
            The value to assign to the entity_details property of this ProblemEntitySummary.
        :type entity_details: list[oci.cloud_guard.models.EntityDetails]

        """
        self.swagger_types = {
            'regions': 'list[str]',
            'time_first_detected': 'datetime',
            'problem_id': 'str',
            'time_last_detected': 'datetime',
            'result_url': 'str',
            'entity_details': 'list[EntityDetails]'
        }

        self.attribute_map = {
            'regions': 'regions',
            'time_first_detected': 'timeFirstDetected',
            'problem_id': 'problemId',
            'time_last_detected': 'timeLastDetected',
            'result_url': 'resultUrl',
            'entity_details': 'entityDetails'
        }

        self._regions = None
        self._time_first_detected = None
        self._problem_id = None
        self._time_last_detected = None
        self._result_url = None
        self._entity_details = None

    @property
    def regions(self):
        """
        **[Required]** Gets the regions of this ProblemEntitySummary.
        Data source problem entities region


        :return: The regions of this ProblemEntitySummary.
        :rtype: list[str]
        """
        return self._regions

    @regions.setter
    def regions(self, regions):
        """
        Sets the regions of this ProblemEntitySummary.
        Data source problem entities region


        :param regions: The regions of this ProblemEntitySummary.
        :type: list[str]
        """
        self._regions = regions

    @property
    def time_first_detected(self):
        """
        **[Required]** Gets the time_first_detected of this ProblemEntitySummary.
        Data source problem entities first detected time


        :return: The time_first_detected of this ProblemEntitySummary.
        :rtype: datetime
        """
        return self._time_first_detected

    @time_first_detected.setter
    def time_first_detected(self, time_first_detected):
        """
        Sets the time_first_detected of this ProblemEntitySummary.
        Data source problem entities first detected time


        :param time_first_detected: The time_first_detected of this ProblemEntitySummary.
        :type: datetime
        """
        self._time_first_detected = time_first_detected

    @property
    def problem_id(self):
        """
        **[Required]** Gets the problem_id of this ProblemEntitySummary.
        Attached problem id


        :return: The problem_id of this ProblemEntitySummary.
        :rtype: str
        """
        return self._problem_id

    @problem_id.setter
    def problem_id(self, problem_id):
        """
        Sets the problem_id of this ProblemEntitySummary.
        Attached problem id


        :param problem_id: The problem_id of this ProblemEntitySummary.
        :type: str
        """
        self._problem_id = problem_id

    @property
    def time_last_detected(self):
        """
        **[Required]** Gets the time_last_detected of this ProblemEntitySummary.
        Data source problem entities last detected time


        :return: The time_last_detected of this ProblemEntitySummary.
        :rtype: datetime
        """
        return self._time_last_detected

    @time_last_detected.setter
    def time_last_detected(self, time_last_detected):
        """
        Sets the time_last_detected of this ProblemEntitySummary.
        Data source problem entities last detected time


        :param time_last_detected: The time_last_detected of this ProblemEntitySummary.
        :type: datetime
        """
        self._time_last_detected = time_last_detected

    @property
    def result_url(self):
        """
        Gets the result_url of this ProblemEntitySummary.
        Log result query url for a data source query


        :return: The result_url of this ProblemEntitySummary.
        :rtype: str
        """
        return self._result_url

    @result_url.setter
    def result_url(self, result_url):
        """
        Sets the result_url of this ProblemEntitySummary.
        Log result query url for a data source query


        :param result_url: The result_url of this ProblemEntitySummary.
        :type: str
        """
        self._result_url = result_url

    @property
    def entity_details(self):
        """
        Gets the entity_details of this ProblemEntitySummary.
        List of event related to a DataSource


        :return: The entity_details of this ProblemEntitySummary.
        :rtype: list[oci.cloud_guard.models.EntityDetails]
        """
        return self._entity_details

    @entity_details.setter
    def entity_details(self, entity_details):
        """
        Sets the entity_details of this ProblemEntitySummary.
        List of event related to a DataSource


        :param entity_details: The entity_details of this ProblemEntitySummary.
        :type: list[oci.cloud_guard.models.EntityDetails]
        """
        self._entity_details = entity_details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other