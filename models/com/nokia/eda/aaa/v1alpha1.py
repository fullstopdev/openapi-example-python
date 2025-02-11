# generated by datamodel-codegen:
#   filename:  https://raw.githubusercontent.com/eda-labs/openapi/main/apps/aaa.eda.nokia.com/v1alpha1/aaa.json
#   timestamp: 2025-01-22T14:25:42+00:00

from __future__ import annotations

from typing import List, Literal, Optional

from pydantic import BaseModel, Field
from typing_extensions import Annotated

from ..... import Metadata


class Rule(BaseModel):
    action: Annotated[
        Literal['Deny', 'ReadWrite', 'Read'],
        Field(description='Set the action for this entry.', title='Action'),
    ]
    match: Annotated[
        Optional[str],
        Field(
            description='Set the match for this entry. This is a string to match input against - for example "interface" for srl or "configure port" for sros.\nRules here should be specified in the target specific format.',
            title='Match',
        ),
    ] = None
    operatingSystem: Annotated[
        Literal['srl', 'sros'],
        Field(
            description='Operating system to match against for this rule.\nOperating system to deploy this rule to.',
            title='Operating System',
        ),
    ]


class Tacacs(BaseModel):
    privilegeLevel: Annotated[
        Optional[int],
        Field(
            description='Set the privilege level for this group.',
            ge=0,
            le=15,
            title='Privilege Level',
        ),
    ] = None


class Spec(BaseModel):
    groupName: Annotated[
        Optional[str],
        Field(
            description='Set the local name for this group. If not provided, the resource name will be used.',
            title='Group Name',
        ),
    ] = None
    rules: Annotated[
        Optional[List[Rule]], Field(description='Rules for this group.', title='Rules')
    ] = None
    services: Annotated[
        List[
            Literal[
                'CLI',
                'FTP',
                'GNMI',
                'GNOI',
                'GNSI',
                'GRIBI',
                'Reflection',
                'JSON-RPC',
                'NETCONF',
            ]
        ],
        Field(description='Enabled services for this group', title='Services'),
    ]
    superuser: Annotated[
        Optional[bool],
        Field(description='Make members of this group superusers.', title='Superuser'),
    ] = None
    tacacs: Annotated[
        Optional[Tacacs], Field(description='TACACS configuration.', title='TACACS')
    ] = None


class Status(BaseModel):
    nodes: Annotated[
        Optional[List[str]],
        Field(
            description='List of TopoNodes group has been deployed to.', title='Nodes'
        ),
    ] = None


class NodeGroup(BaseModel):
    apiVersion: str
    kind: str
    metadata: Metadata
    spec: Annotated[
        Spec,
        Field(
            description='NodeGroup is a representation of a group on a node, including the services it has access to, any RBAC, and TACACS configuration.\nNodeGroups are deployed to nodes by NodeUser or other permission-consuming resources.',
            title='Specification',
        ),
    ]
    status: Annotated[
        Optional[Status],
        Field(description='Deployment status of this NodeGroup.', title='Status'),
    ] = None


class NodeGroupList(BaseModel):
    apiVersion: str
    items: Optional[List[NodeGroup]] = None
    kind: str
