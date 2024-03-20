# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "afd profile create",
)
class Create(AAZCommand):
    """Create a new Azure Front Door Standard or Azure Front Door Premium or CDN profile with a profile name under the specified subscription and resource group.

    :example: Create an AFD profile using Standard SKU.
        az afd profile create -g group --profile-name profile --sku Standard_AzureFrontDoor
    """

    _aaz_info = {
        "version": "2023-05-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.cdn/profiles/{}", "2023-05-01"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_lro_poller(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.profile_name = AAZStrArg(
            options=["-n", "--name", "--profile-name"],
            help="Name of the Azure Front Door Standard or Azure Front Door Premium or CDN profile which is unique within the resource group.",
            required=True,
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )

        # define Arg Group "Profile"

        _args_schema = cls._args_schema
        _args_schema.identity = AAZObjectArg(
            options=["--identity"],
            arg_group="Profile",
            help="Managed service identity (system assigned and/or user assigned identities).",
        )
        _args_schema.location = AAZResourceLocationArg(
            arg_group="Profile",
            help="Resource location.",
            required=True,
            fmt=AAZResourceLocationArgFormat(
                resource_group_arg="resource_group",
            ),
        )
        _args_schema.tags = AAZDictArg(
            options=["--tags"],
            arg_group="Profile",
            help="Resource tags.",
        )

        identity = cls._args_schema.identity
        identity.type = AAZStrArg(
            options=["type"],
            help="Type of managed service identity (where both SystemAssigned and UserAssigned types are allowed).",
            required=True,
            enum={"None": "None", "SystemAssigned": "SystemAssigned", "SystemAssigned, UserAssigned": "SystemAssigned, UserAssigned", "UserAssigned": "UserAssigned"},
        )
        identity.user_assigned_identities = AAZDictArg(
            options=["user-assigned-identities"],
            help="The set of user assigned identities associated with the resource. The userAssignedIdentities dictionary keys will be ARM resource ids in the form: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}. The dictionary values can be empty objects ({}) in requests.",
        )

        user_assigned_identities = cls._args_schema.identity.user_assigned_identities
        user_assigned_identities.Element = AAZObjectArg(
            blank={},
        )

        tags = cls._args_schema.tags
        tags.Element = AAZStrArg()

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.origin_response_timeout_seconds = AAZIntArg(
            options=["--origin-response-timeout-seconds"],
            arg_group="Properties",
            help="Send and receive timeout on forwarding request to the origin. When timeout is reached, the request fails and returns.",
            fmt=AAZIntArgFormat(
                minimum=16,
            ),
        )

        # define Arg Group "Sku"

        _args_schema = cls._args_schema
        _args_schema.sku = AAZStrArg(
            options=["--sku"],
            arg_group="Sku",
            help="Name of the pricing tier.",
            enum={"Custom_Verizon": "Custom_Verizon", "Premium_AzureFrontDoor": "Premium_AzureFrontDoor", "Premium_Verizon": "Premium_Verizon", "StandardPlus_955BandWidth_ChinaCdn": "StandardPlus_955BandWidth_ChinaCdn", "StandardPlus_AvgBandWidth_ChinaCdn": "StandardPlus_AvgBandWidth_ChinaCdn", "StandardPlus_ChinaCdn": "StandardPlus_ChinaCdn", "Standard_955BandWidth_ChinaCdn": "Standard_955BandWidth_ChinaCdn", "Standard_Akamai": "Standard_Akamai", "Standard_AvgBandWidth_ChinaCdn": "Standard_AvgBandWidth_ChinaCdn", "Standard_AzureFrontDoor": "Standard_AzureFrontDoor", "Standard_ChinaCdn": "Standard_ChinaCdn", "Standard_Microsoft": "Standard_Microsoft", "Standard_Verizon": "Standard_Verizon"},
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        yield self.ProfilesCreate(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class ProfilesCreate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200, 201]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "profileName", self.ctx.args.profile_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2023-05-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                typ=AAZObjectType,
                typ_kwargs={"flags": {"required": True, "client_flatten": True}}
            )
            _builder.set_prop("identity", AAZObjectType, ".identity")
            _builder.set_prop("location", AAZStrType, ".location", typ_kwargs={"flags": {"required": True}})
            _builder.set_prop("properties", AAZObjectType, typ_kwargs={"flags": {"client_flatten": True}})
            _builder.set_prop("sku", AAZObjectType, ".", typ_kwargs={"flags": {"required": True}})
            _builder.set_prop("tags", AAZDictType, ".tags")

            identity = _builder.get(".identity")
            if identity is not None:
                identity.set_prop("type", AAZStrType, ".type", typ_kwargs={"flags": {"required": True}})
                identity.set_prop("userAssignedIdentities", AAZDictType, ".user_assigned_identities")

            user_assigned_identities = _builder.get(".identity.userAssignedIdentities")
            if user_assigned_identities is not None:
                user_assigned_identities.set_elements(AAZObjectType, ".")

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("originResponseTimeoutSeconds", AAZIntType, ".origin_response_timeout_seconds")

            sku = _builder.get(".sku")
            if sku is not None:
                sku.set_prop("name", AAZStrType, ".sku")

            tags = _builder.get(".tags")
            if tags is not None:
                tags.set_elements(AAZStrType, ".")

            return self.serialize_content(_content_value)

        def on_200_201(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200_201
            )

        _schema_on_200_201 = None

        @classmethod
        def _build_schema_on_200_201(cls):
            if cls._schema_on_200_201 is not None:
                return cls._schema_on_200_201

            cls._schema_on_200_201 = AAZObjectType()
            _CreateHelper._build_schema_profile_read(cls._schema_on_200_201)

            return cls._schema_on_200_201


class _CreateHelper:
    """Helper class for Create"""

    _schema_profile_read = None

    @classmethod
    def _build_schema_profile_read(cls, _schema):
        if cls._schema_profile_read is not None:
            _schema.id = cls._schema_profile_read.id
            _schema.identity = cls._schema_profile_read.identity
            _schema.kind = cls._schema_profile_read.kind
            _schema.location = cls._schema_profile_read.location
            _schema.name = cls._schema_profile_read.name
            _schema.properties = cls._schema_profile_read.properties
            _schema.sku = cls._schema_profile_read.sku
            _schema.system_data = cls._schema_profile_read.system_data
            _schema.tags = cls._schema_profile_read.tags
            _schema.type = cls._schema_profile_read.type
            return

        cls._schema_profile_read = _schema_profile_read = AAZObjectType()

        profile_read = _schema_profile_read
        profile_read.id = AAZStrType(
            flags={"read_only": True},
        )
        profile_read.identity = AAZObjectType()
        profile_read.kind = AAZStrType(
            flags={"read_only": True},
        )
        profile_read.location = AAZStrType(
            flags={"required": True},
        )
        profile_read.name = AAZStrType(
            flags={"read_only": True},
        )
        profile_read.properties = AAZObjectType(
            flags={"client_flatten": True},
        )
        profile_read.sku = AAZObjectType(
            flags={"required": True},
        )
        profile_read.system_data = AAZObjectType(
            serialized_name="systemData",
            flags={"read_only": True},
        )
        profile_read.tags = AAZDictType()
        profile_read.type = AAZStrType(
            flags={"read_only": True},
        )

        identity = _schema_profile_read.identity
        identity.principal_id = AAZStrType(
            serialized_name="principalId",
            flags={"read_only": True},
        )
        identity.tenant_id = AAZStrType(
            serialized_name="tenantId",
            flags={"read_only": True},
        )
        identity.type = AAZStrType(
            flags={"required": True},
        )
        identity.user_assigned_identities = AAZDictType(
            serialized_name="userAssignedIdentities",
        )

        user_assigned_identities = _schema_profile_read.identity.user_assigned_identities
        user_assigned_identities.Element = AAZObjectType()

        _element = _schema_profile_read.identity.user_assigned_identities.Element
        _element.client_id = AAZStrType(
            serialized_name="clientId",
            flags={"read_only": True},
        )
        _element.principal_id = AAZStrType(
            serialized_name="principalId",
            flags={"read_only": True},
        )

        properties = _schema_profile_read.properties
        properties.extended_properties = AAZDictType(
            serialized_name="extendedProperties",
            flags={"read_only": True},
        )
        properties.front_door_id = AAZStrType(
            serialized_name="frontDoorId",
            flags={"read_only": True},
        )
        properties.origin_response_timeout_seconds = AAZIntType(
            serialized_name="originResponseTimeoutSeconds",
        )
        properties.provisioning_state = AAZStrType(
            serialized_name="provisioningState",
            flags={"read_only": True},
        )
        properties.resource_state = AAZStrType(
            serialized_name="resourceState",
            flags={"read_only": True},
        )

        extended_properties = _schema_profile_read.properties.extended_properties
        extended_properties.Element = AAZStrType()

        sku = _schema_profile_read.sku
        sku.name = AAZStrType()

        system_data = _schema_profile_read.system_data
        system_data.created_at = AAZStrType(
            serialized_name="createdAt",
        )
        system_data.created_by = AAZStrType(
            serialized_name="createdBy",
        )
        system_data.created_by_type = AAZStrType(
            serialized_name="createdByType",
        )
        system_data.last_modified_at = AAZStrType(
            serialized_name="lastModifiedAt",
        )
        system_data.last_modified_by = AAZStrType(
            serialized_name="lastModifiedBy",
        )
        system_data.last_modified_by_type = AAZStrType(
            serialized_name="lastModifiedByType",
        )

        tags = _schema_profile_read.tags
        tags.Element = AAZStrType()

        _schema.id = cls._schema_profile_read.id
        _schema.identity = cls._schema_profile_read.identity
        _schema.kind = cls._schema_profile_read.kind
        _schema.location = cls._schema_profile_read.location
        _schema.name = cls._schema_profile_read.name
        _schema.properties = cls._schema_profile_read.properties
        _schema.sku = cls._schema_profile_read.sku
        _schema.system_data = cls._schema_profile_read.system_data
        _schema.tags = cls._schema_profile_read.tags
        _schema.type = cls._schema_profile_read.type


__all__ = ["Create"]
