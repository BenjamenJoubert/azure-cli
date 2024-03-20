# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command_group(
    "cdn origin",
)
class __CMDGroup(AAZCommandGroup):
    """List or show existing origins related to CDN endpoints.
    """
    pass


__all__ = ["__CMDGroup"]
