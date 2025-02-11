# generated by datamodel-codegen:
#   filename:  https://raw.githubusercontent.com/eda-labs/openapi/main/apps/config.eda.nokia.com/v1alpha1/config.json
#   timestamp: 2025-01-22T14:25:50+00:00

from __future__ import annotations

from typing import List, Literal, Optional

from pydantic import BaseModel, Field
from typing_extensions import Annotated

from ..... import Metadata


class Config(BaseModel):
    config: Annotated[
        str,
        Field(
            description='JSON-formatted string representing the configuration to apply.',
            title='Configuration',
        ),
    ]
    operation: Annotated[
        Literal['Create', 'Update', 'Delete'],
        Field(
            description='Indicates the operation in which to apply the configuration.',
            title='Operation',
        ),
    ]
    path: Annotated[
        str,
        Field(
            description='Path to apply the configuration in jspath notation, including any keys if relevant, e.g. .system.information.',
            title='Path',
        ),
    ]


class Spec(BaseModel):
    configs: Annotated[
        List[Config],
        Field(
            description='Configurations to apply, being sets of paths, operations and JSON configurations.',
            title='Configurations',
        ),
    ]
    endpointSelector: Annotated[
        Optional[List[str]],
        Field(
            description='Label selector to use to match targets to deploy Configlet to.',
            title='Target Selector',
        ),
    ] = None
    endpoints: Annotated[
        Optional[List[str]],
        Field(
            description='Reference to targets to deploy Configlet to.', title='Targets'
        ),
    ] = None
    operatingSystem: Annotated[
        Optional[Literal['srl', 'sros']],
        Field(
            description='Operating system to match against when selecting targets.',
            title='Operating System',
        ),
    ] = None
    priority: Annotated[
        Optional[int],
        Field(
            description='Priority of this Configlet, between -100 and 100. Higher priorities overwrite lower priorities in the event of conflicts.',
            ge=-100,
            le=100,
            title='Priority',
        ),
    ] = 0
    version: Annotated[
        Optional[str],
        Field(
            description='Version to match against when selecting targets.',
            title='Version',
        ),
    ] = None


class Status(BaseModel):
    endpoints: Annotated[
        Optional[List[str]],
        Field(
            description='List of targets this configlet has been applied to.',
            title='Targets',
        ),
    ] = None


class Configlet(BaseModel):
    apiVersion: str
    kind: str
    metadata: Metadata
    spec: Annotated[
        Spec,
        Field(
            description='Configlet is a configuration snippet that can be applied to a set of targets.\nThe path on the target is provided in jspath notation, and the configuration is provided as a JSON string.\nConfiglets can be applied to a set of targets based on a label selector, a list of targets, or a combination of both.',
            title='Specification',
        ),
    ]
    status: Annotated[
        Optional[Status],
        Field(description='Deployment status of this Configlet.', title='Status'),
    ] = None


class ConfigletList(BaseModel):
    apiVersion: str
    items: Optional[List[Configlet]] = None
    kind: str
