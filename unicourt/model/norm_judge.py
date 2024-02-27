"""
    UniCourt Enterprise APIs

    <button><a href=\"/enterpriseapi/download/UniCourt-Enterprise-API-Spec.yaml\" >Download UniCourt Enterprise APIs Specification</a></button>   # noqa: E501

    The version of the OpenAPI document: 
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from unicourt.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from unicourt.exceptions import ApiAttributeError


def lazy_import():
    from unicourt.model.case_analytics_api import CaseAnalyticsAPI
    from unicourt.model.judge_analytics_api import JudgeAnalyticsAPI
    from unicourt.model.norm_judge_public_data import NormJudgePublicData
    globals()['CaseAnalyticsAPI'] = CaseAnalyticsAPI
    globals()['JudgeAnalyticsAPI'] = JudgeAnalyticsAPI
    globals()['NormJudgePublicData'] = NormJudgePublicData


class NormJudge(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
        ('object',): {
            'max_length': 9,
        },
        ('norm_judge_id',): {
            'max_length': 18,
            'min_length': 18,
        },
        ('name',): {
            'max_length': 500,
        },
        ('first_name',): {
            'max_length': 500,
        },
        ('middle_name',): {
            'max_length': 500,
        },
        ('last_name',): {
            'max_length': 500,
        },
        ('case_search_api',): {
            'max_length': 255,
        },
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'object': (str,),  # noqa: E501
            'norm_judge_id': (str,),  # noqa: E501
            'name': (str,),  # noqa: E501
            'first_name': (str,),  # noqa: E501
            'middle_name': (str, none_type,),  # noqa: E501
            'last_name': (str,),  # noqa: E501
            'case_search_api': (str,),  # noqa: E501
            'case_analytics_api': (CaseAnalyticsAPI,),  # noqa: E501
            'has_associated_public_data': (bool,),  # noqa: E501
            'judicial_data_array': ([NormJudgePublicData],),  # noqa: E501
            'judge_analytics_api': (JudgeAnalyticsAPI,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'object': 'object',  # noqa: E501
        'norm_judge_id': 'normJudgeId',  # noqa: E501
        'name': 'name',  # noqa: E501
        'first_name': 'firstName',  # noqa: E501
        'middle_name': 'middleName',  # noqa: E501
        'last_name': 'lastName',  # noqa: E501
        'case_search_api': 'caseSearchAPI',  # noqa: E501
        'case_analytics_api': 'caseAnalyticsAPI',  # noqa: E501
        'has_associated_public_data': 'hasAssociatedPublicData',  # noqa: E501
        'judicial_data_array': 'judicialDataArray',  # noqa: E501
        'judge_analytics_api': 'judgeAnalyticsAPI',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, norm_judge_id, name, first_name, middle_name, last_name, case_search_api, case_analytics_api, has_associated_public_data, judicial_data_array, judge_analytics_api, *args, **kwargs):  # noqa: E501
        """NormJudge - a model defined in OpenAPI

        Args:
            norm_judge_id (str):
            name (str):
            first_name (str):
            middle_name (str, none_type):
            last_name (str):
            case_search_api (str):
            case_analytics_api (CaseAnalyticsAPI):
            has_associated_public_data (bool):
            judicial_data_array ([NormJudgePublicData]):
            judge_analytics_api (JudgeAnalyticsAPI):

        Keyword Args:
            object (str): defaults to "NormJudge"  # noqa: E501
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
        """

        object = kwargs.get('object', "NormJudge")
        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', True)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.object = object
        self.norm_judge_id = norm_judge_id
        self.name = name
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.case_search_api = case_search_api
        self.case_analytics_api = case_analytics_api
        self.has_associated_public_data = has_associated_public_data
        self.judicial_data_array = judicial_data_array
        self.judge_analytics_api = judge_analytics_api
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, norm_judge_id, name, first_name, middle_name, last_name, case_search_api, case_analytics_api, has_associated_public_data, judicial_data_array, judge_analytics_api, *args, **kwargs):  # noqa: E501
        """NormJudge - a model defined in OpenAPI

        Args:
            norm_judge_id (str):
            name (str):
            first_name (str):
            middle_name (str, none_type):
            last_name (str):
            case_search_api (str):
            case_analytics_api (CaseAnalyticsAPI):
            has_associated_public_data (bool):
            judicial_data_array ([NormJudgePublicData]):
            judge_analytics_api (JudgeAnalyticsAPI):

        Keyword Args:
            object (str): defaults to "NormJudge"  # noqa: E501
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
        """

        object = kwargs.get('object', "NormJudge")
        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.object = object
        self.norm_judge_id = norm_judge_id
        self.name = name
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.case_search_api = case_search_api
        self.case_analytics_api = case_analytics_api
        self.has_associated_public_data = has_associated_public_data
        self.judicial_data_array = judicial_data_array
        self.judge_analytics_api = judge_analytics_api
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
