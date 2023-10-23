# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .data_entity import DataEntity
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DerivedEntity(DataEntity):
    """
    The Derive entity object
    """

    #: A constant which can be used with the mode property of a DerivedEntity.
    #: This constant has a value of "IN"
    MODE_IN = "IN"

    #: A constant which can be used with the mode property of a DerivedEntity.
    #: This constant has a value of "OUT"
    MODE_OUT = "OUT"

    def __init__(self, **kwargs):
        """
        Initializes a new DerivedEntity object with values from keyword arguments. The default value of the :py:attr:`~oci.data_connectivity.models.DerivedEntity.model_type` attribute
        of this class is ``DERIVED_ENTITY`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param entity_properties:
            The value to assign to the entity_properties property of this DerivedEntity.
        :type entity_properties: dict(str, str)

        :param model_type:
            The value to assign to the model_type property of this DerivedEntity.
            Allowed values for this property are: "VIEW_ENTITY", "TABLE_ENTITY", "FILE_ENTITY", "DATA_STORE_ENTITY", "SQL_ENTITY", "DERIVED_ENTITY", "MESSAGE_ENTITY", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type model_type: str

        :param metadata:
            The value to assign to the metadata property of this DerivedEntity.
        :type metadata: oci.data_connectivity.models.ObjectMetadata

        :param key:
            The value to assign to the key property of this DerivedEntity.
        :type key: str

        :param model_version:
            The value to assign to the model_version property of this DerivedEntity.
        :type model_version: str

        :param parent_ref:
            The value to assign to the parent_ref property of this DerivedEntity.
        :type parent_ref: oci.data_connectivity.models.ParentReference

        :param name:
            The value to assign to the name property of this DerivedEntity.
        :type name: str

        :param object_version:
            The value to assign to the object_version property of this DerivedEntity.
        :type object_version: int

        :param shape:
            The value to assign to the shape property of this DerivedEntity.
        :type shape: oci.data_connectivity.models.Shape

        :param shape_id:
            The value to assign to the shape_id property of this DerivedEntity.
        :type shape_id: str

        :param resource_name:
            The value to assign to the resource_name property of this DerivedEntity.
        :type resource_name: str

        :param object_status:
            The value to assign to the object_status property of this DerivedEntity.
        :type object_status: int

        :param identifier:
            The value to assign to the identifier property of this DerivedEntity.
        :type identifier: str

        :param ref_data_object:
            The value to assign to the ref_data_object property of this DerivedEntity.
        :type ref_data_object: oci.data_connectivity.models.ReferencedDataObject

        :param mode:
            The value to assign to the mode property of this DerivedEntity.
            Allowed values for this property are: "IN", "OUT", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type mode: str

        :param derived_properties:
            The value to assign to the derived_properties property of this DerivedEntity.
        :type derived_properties: dict(str, object)

        """
        self.swagger_types = {
            'entity_properties': 'dict(str, str)',
            'model_type': 'str',
            'metadata': 'ObjectMetadata',
            'key': 'str',
            'model_version': 'str',
            'parent_ref': 'ParentReference',
            'name': 'str',
            'object_version': 'int',
            'shape': 'Shape',
            'shape_id': 'str',
            'resource_name': 'str',
            'object_status': 'int',
            'identifier': 'str',
            'ref_data_object': 'ReferencedDataObject',
            'mode': 'str',
            'derived_properties': 'dict(str, object)'
        }

        self.attribute_map = {
            'entity_properties': 'entityProperties',
            'model_type': 'modelType',
            'metadata': 'metadata',
            'key': 'key',
            'model_version': 'modelVersion',
            'parent_ref': 'parentRef',
            'name': 'name',
            'object_version': 'objectVersion',
            'shape': 'shape',
            'shape_id': 'shapeId',
            'resource_name': 'resourceName',
            'object_status': 'objectStatus',
            'identifier': 'identifier',
            'ref_data_object': 'refDataObject',
            'mode': 'mode',
            'derived_properties': 'derivedProperties'
        }

        self._entity_properties = None
        self._model_type = None
        self._metadata = None
        self._key = None
        self._model_version = None
        self._parent_ref = None
        self._name = None
        self._object_version = None
        self._shape = None
        self._shape_id = None
        self._resource_name = None
        self._object_status = None
        self._identifier = None
        self._ref_data_object = None
        self._mode = None
        self._derived_properties = None
        self._model_type = 'DERIVED_ENTITY'

    @property
    def key(self):
        """
        Gets the key of this DerivedEntity.
        The object key.


        :return: The key of this DerivedEntity.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this DerivedEntity.
        The object key.


        :param key: The key of this DerivedEntity.
        :type: str
        """
        self._key = key

    @property
    def model_version(self):
        """
        Gets the model_version of this DerivedEntity.
        The object's model version.


        :return: The model_version of this DerivedEntity.
        :rtype: str
        """
        return self._model_version

    @model_version.setter
    def model_version(self, model_version):
        """
        Sets the model_version of this DerivedEntity.
        The object's model version.


        :param model_version: The model_version of this DerivedEntity.
        :type: str
        """
        self._model_version = model_version

    @property
    def parent_ref(self):
        """
        Gets the parent_ref of this DerivedEntity.

        :return: The parent_ref of this DerivedEntity.
        :rtype: oci.data_connectivity.models.ParentReference
        """
        return self._parent_ref

    @parent_ref.setter
    def parent_ref(self, parent_ref):
        """
        Sets the parent_ref of this DerivedEntity.

        :param parent_ref: The parent_ref of this DerivedEntity.
        :type: oci.data_connectivity.models.ParentReference
        """
        self._parent_ref = parent_ref

    @property
    def name(self):
        """
        **[Required]** Gets the name of this DerivedEntity.
        Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is unique, editable and is restricted to 1000 characters.


        :return: The name of this DerivedEntity.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this DerivedEntity.
        Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is unique, editable and is restricted to 1000 characters.


        :param name: The name of this DerivedEntity.
        :type: str
        """
        self._name = name

    @property
    def object_version(self):
        """
        Gets the object_version of this DerivedEntity.
        The version of the object that is used to track changes in the object instance.


        :return: The object_version of this DerivedEntity.
        :rtype: int
        """
        return self._object_version

    @object_version.setter
    def object_version(self, object_version):
        """
        Sets the object_version of this DerivedEntity.
        The version of the object that is used to track changes in the object instance.


        :param object_version: The object_version of this DerivedEntity.
        :type: int
        """
        self._object_version = object_version

    @property
    def shape(self):
        """
        Gets the shape of this DerivedEntity.

        :return: The shape of this DerivedEntity.
        :rtype: oci.data_connectivity.models.Shape
        """
        return self._shape

    @shape.setter
    def shape(self, shape):
        """
        Sets the shape of this DerivedEntity.

        :param shape: The shape of this DerivedEntity.
        :type: oci.data_connectivity.models.Shape
        """
        self._shape = shape

    @property
    def shape_id(self):
        """
        Gets the shape_id of this DerivedEntity.
        The shape ID.


        :return: The shape_id of this DerivedEntity.
        :rtype: str
        """
        return self._shape_id

    @shape_id.setter
    def shape_id(self, shape_id):
        """
        Sets the shape_id of this DerivedEntity.
        The shape ID.


        :param shape_id: The shape_id of this DerivedEntity.
        :type: str
        """
        self._shape_id = shape_id

    @property
    def resource_name(self):
        """
        **[Required]** Gets the resource_name of this DerivedEntity.
        The resource name.


        :return: The resource_name of this DerivedEntity.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        """
        Sets the resource_name of this DerivedEntity.
        The resource name.


        :param resource_name: The resource_name of this DerivedEntity.
        :type: str
        """
        self._resource_name = resource_name

    @property
    def object_status(self):
        """
        Gets the object_status of this DerivedEntity.
        The status of an object that can be set to value 1 for shallow reference across objects, other values reserved.


        :return: The object_status of this DerivedEntity.
        :rtype: int
        """
        return self._object_status

    @object_status.setter
    def object_status(self, object_status):
        """
        Sets the object_status of this DerivedEntity.
        The status of an object that can be set to value 1 for shallow reference across objects, other values reserved.


        :param object_status: The object_status of this DerivedEntity.
        :type: int
        """
        self._object_status = object_status

    @property
    def identifier(self):
        """
        Gets the identifier of this DerivedEntity.
        Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.


        :return: The identifier of this DerivedEntity.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """
        Sets the identifier of this DerivedEntity.
        Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.


        :param identifier: The identifier of this DerivedEntity.
        :type: str
        """
        self._identifier = identifier

    @property
    def ref_data_object(self):
        """
        Gets the ref_data_object of this DerivedEntity.

        :return: The ref_data_object of this DerivedEntity.
        :rtype: oci.data_connectivity.models.ReferencedDataObject
        """
        return self._ref_data_object

    @ref_data_object.setter
    def ref_data_object(self, ref_data_object):
        """
        Sets the ref_data_object of this DerivedEntity.

        :param ref_data_object: The ref_data_object of this DerivedEntity.
        :type: oci.data_connectivity.models.ReferencedDataObject
        """
        self._ref_data_object = ref_data_object

    @property
    def mode(self):
        """
        Gets the mode of this DerivedEntity.
        Determines whether entity is treated as source or target

        Allowed values for this property are: "IN", "OUT", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The mode of this DerivedEntity.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """
        Sets the mode of this DerivedEntity.
        Determines whether entity is treated as source or target


        :param mode: The mode of this DerivedEntity.
        :type: str
        """
        allowed_values = ["IN", "OUT"]
        if not value_allowed_none_or_none_sentinel(mode, allowed_values):
            mode = 'UNKNOWN_ENUM_VALUE'
        self._mode = mode

    @property
    def derived_properties(self):
        """
        Gets the derived_properties of this DerivedEntity.
        Property-bag (key-value pairs where key is Shape Field resource name and value is object)


        :return: The derived_properties of this DerivedEntity.
        :rtype: dict(str, object)
        """
        return self._derived_properties

    @derived_properties.setter
    def derived_properties(self, derived_properties):
        """
        Sets the derived_properties of this DerivedEntity.
        Property-bag (key-value pairs where key is Shape Field resource name and value is object)


        :param derived_properties: The derived_properties of this DerivedEntity.
        :type: dict(str, object)
        """
        self._derived_properties = derived_properties

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other