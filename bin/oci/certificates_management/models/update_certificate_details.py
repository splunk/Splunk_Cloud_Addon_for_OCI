# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateCertificateDetails(object):
    """
    The details of the certificate to update.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateCertificateDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param description:
            The value to assign to the description property of this UpdateCertificateDetails.
        :type description: str

        :param current_version_number:
            The value to assign to the current_version_number property of this UpdateCertificateDetails.
        :type current_version_number: int

        :param certificate_config:
            The value to assign to the certificate_config property of this UpdateCertificateDetails.
        :type certificate_config: oci.certificates_management.models.UpdateCertificateConfigDetails

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateCertificateDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateCertificateDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param certificate_rules:
            The value to assign to the certificate_rules property of this UpdateCertificateDetails.
        :type certificate_rules: list[oci.certificates_management.models.CertificateRule]

        """
        self.swagger_types = {
            'description': 'str',
            'current_version_number': 'int',
            'certificate_config': 'UpdateCertificateConfigDetails',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'certificate_rules': 'list[CertificateRule]'
        }

        self.attribute_map = {
            'description': 'description',
            'current_version_number': 'currentVersionNumber',
            'certificate_config': 'certificateConfig',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'certificate_rules': 'certificateRules'
        }

        self._description = None
        self._current_version_number = None
        self._certificate_config = None
        self._freeform_tags = None
        self._defined_tags = None
        self._certificate_rules = None

    @property
    def description(self):
        """
        Gets the description of this UpdateCertificateDetails.
        A brief description of the certificate. Avoid entering confidential information.


        :return: The description of this UpdateCertificateDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this UpdateCertificateDetails.
        A brief description of the certificate. Avoid entering confidential information.


        :param description: The description of this UpdateCertificateDetails.
        :type: str
        """
        self._description = description

    @property
    def current_version_number(self):
        """
        Gets the current_version_number of this UpdateCertificateDetails.
        Makes this version the current version. This property cannot be updated in combination with any other properties.


        :return: The current_version_number of this UpdateCertificateDetails.
        :rtype: int
        """
        return self._current_version_number

    @current_version_number.setter
    def current_version_number(self, current_version_number):
        """
        Sets the current_version_number of this UpdateCertificateDetails.
        Makes this version the current version. This property cannot be updated in combination with any other properties.


        :param current_version_number: The current_version_number of this UpdateCertificateDetails.
        :type: int
        """
        self._current_version_number = current_version_number

    @property
    def certificate_config(self):
        """
        Gets the certificate_config of this UpdateCertificateDetails.

        :return: The certificate_config of this UpdateCertificateDetails.
        :rtype: oci.certificates_management.models.UpdateCertificateConfigDetails
        """
        return self._certificate_config

    @certificate_config.setter
    def certificate_config(self, certificate_config):
        """
        Sets the certificate_config of this UpdateCertificateDetails.

        :param certificate_config: The certificate_config of this UpdateCertificateDetails.
        :type: oci.certificates_management.models.UpdateCertificateConfigDetails
        """
        self._certificate_config = certificate_config

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateCertificateDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this UpdateCertificateDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateCertificateDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this UpdateCertificateDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateCertificateDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this UpdateCertificateDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateCertificateDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this UpdateCertificateDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def certificate_rules(self):
        """
        Gets the certificate_rules of this UpdateCertificateDetails.
        An optional list of rules that control how the certificate is used and managed.


        :return: The certificate_rules of this UpdateCertificateDetails.
        :rtype: list[oci.certificates_management.models.CertificateRule]
        """
        return self._certificate_rules

    @certificate_rules.setter
    def certificate_rules(self, certificate_rules):
        """
        Sets the certificate_rules of this UpdateCertificateDetails.
        An optional list of rules that control how the certificate is used and managed.


        :param certificate_rules: The certificate_rules of this UpdateCertificateDetails.
        :type: list[oci.certificates_management.models.CertificateRule]
        """
        self._certificate_rules = certificate_rules

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other