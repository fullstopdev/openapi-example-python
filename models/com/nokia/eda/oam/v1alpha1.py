# generated by datamodel-codegen:
#   filename:  https://raw.githubusercontent.com/eda-labs/openapi/main/apps/oam.eda.nokia.com/v1alpha1/oam.json
#   timestamp: 2025-01-22T14:26:02+00:00

from __future__ import annotations

from datetime import date
from typing import List, Literal, Optional

from pydantic import BaseModel, Field
from typing_extensions import Annotated

from ..... import Metadata


class LocalDestination(BaseModel):
    interface: Annotated[
        Optional[str],
        Field(
            description='Reference to an Interface resource to send the mirrored traffic to.  This must be on the same Node as the source.',
            title='Local Interface',
        ),
    ] = None
    vlanID: Annotated[
        Optional[str],
        Field(
            description='Single value between 0-4094 support, or the special keyword untagged.',
            title='VLAN ID',
        ),
    ] = None


class RemoteDestination(BaseModel):
    defaultRouter: Annotated[
        Optional[str],
        Field(
            description='Specifies the DefaultRouter to reach the remote destination of the mirror, a Router and DefaultRouter reference cannot be set at the same time.',
            title='Default Router',
        ),
    ] = None
    destinationIP: Annotated[
        Optional[str],
        Field(
            description='Remote destination IP address.  When a remote destination is used for the mirror, the destinationIP is mandatory.',
            title='Destination IP',
        ),
    ] = None
    encapsulation: Annotated[
        Optional[Literal['L2OGRE', 'L3OGRE']], Field(title='Encapsulation')
    ] = None
    router: Annotated[
        Optional[str],
        Field(
            description='Specifies the Router to reach the remote destination of the mirror, a Router and DefaultRouter reference cannot be set at the same time.',
            title='Router',
        ),
    ] = None
    sourceIP: Annotated[
        Optional[str],
        Field(
            description='Source IP to use when sending a mirror to a remote destination.  When a remote destination us used for the mirror, the sourceIP is mandatory.',
            title='Source IP',
        ),
    ] = None


class RateLimit(BaseModel):
    burstSize: Annotated[
        Optional[int],
        Field(description='The maximum burst size in bytes.', title='Burst Size'),
    ] = None
    entrySpecificPolicer: Annotated[
        Optional[bool],
        Field(
            description='Controls policer instantiation: false for shared instance, true for per-entry instances',
            title='Entry Specific Policer',
        ),
    ] = False
    peakRate: Annotated[
        Optional[int],
        Field(description='The peak rate in kilobytes per second.', title='Peak Rate'),
    ] = None
    scope: Annotated[
        Optional[Literal['Global', 'Subinterface']],
        Field(
            description='Determines how the policer is applied across subinterfaces. Global applies the policer across all subinterfaces, while Subinterface applies it individually to each subinterface.',
            title='Scope',
        ),
    ] = 'Global'


class IpEntry(BaseModel):
    action: Annotated[
        Optional[Literal['Drop', 'Accept', 'RateLimit']],
        Field(
            description="An action to take, either 'accept', or 'drop'.", title='Action'
        ),
    ] = None
    destinationPortName: Annotated[
        Optional[
            Literal[
                'ACAP',
                'AFP-TCP',
                'ARNS',
                'ASF-RMCP',
                'ASHARE',
                'ATALK-RM',
                'AURP',
                'AUTH',
                'BFD',
                'BFD-ECHO',
                'BFTP',
                'BGMP',
                'BGP',
                'BOOTPC',
                'BOOTPS',
                'CCSO-NS',
                'CHARGEN',
                'CISCO-TDP',
                'CITADEL',
                'CLEARCASE',
                'COMMERCE',
                'COURIER',
                'DAYTIME',
                'DHCP-FAILOVER',
                'DHCPV6-CLIENT',
                'DHCPV6-SERVER',
                'DICOM',
                'DISCARD',
                'DNSIX',
                'DOMAIN',
                'DSP',
                'ECHO',
                'EPP',
                'ESRO',
                'EXEC',
                'FINGER',
                'FTP',
                'FTP-DATA',
                'FTPS',
                'FTPS-DATA',
                'GODI',
                'GOPHER',
                'GTP-C',
                'GTP-PRIME',
                'GTP-U',
                'HA-CLUSTER',
                'HOSTNAME',
                'HP-ALARM-MGR',
                'HTTP',
                'HTTP-ALT',
                'HTTP-MGMT',
                'HTTP-RPC',
                'HTTPS',
                'IEEE-MMS-SSL',
                'IMAP',
                'IMAP3',
                'IMAPS',
                'IPP',
                'IPSEC',
                'IPX',
                'IRC',
                'IRIS-BEEP',
                'ISAKMP',
                'ISAKMP-NAT',
                'ISCSI',
                'ISO-TSAP',
                'KERBEROS',
                'KERBEROS-ADM',
                'KLOGIN',
                'KPASSWD',
                'KSHELL',
                'L2TP',
                'LDAP',
                'LDAPS',
                'LDP',
                'LMP',
                'LOGIN',
                'LPD',
                'LSP-PING',
                'MAC-SERVER-ADM',
                'MATIP-A',
                'MATIP-B',
                'MICRO-BFD',
                'MICROSOFT-DS',
                'MOBILE-IP',
                'MONITOR',
                'MPP',
                'MS-EXCHANGE',
                'MSDP',
                'MSP',
                'MSSQL-M',
                'MSSQL-S',
                'MULTIHOP-BFD',
                'NAS',
                'NCP',
                'NETBIOS-DATA',
                'NETBIOS-NS',
                'NETBIOS-SS',
                'NETNEWS',
                'NETRJS-1',
                'NETRJS-2',
                'NETRJS-3',
                'NETRJS-4',
                'NETWALL',
                'NEW-RWHO',
                'NFS',
                'NNTP',
                'NNTPS',
                'NTP',
                'ODMR',
                'OLSR',
                'OPENVPN',
                'PIM-AUTO-RP',
                'PKIX-TIMESTAMP',
                'POP2',
                'POP3',
                'POP3S',
                'PPTP',
                'PRINT-SRV',
                'PTP-EVENT',
                'PTP-GENERAL',
                'QMTP',
                'QOTD',
                'RADIUS',
            ]
        ],
        Field(
            description='Destination port to match by name.',
            title='Destination Port Name',
        ),
    ] = None
    destinationPortNumber: Annotated[
        Optional[int],
        Field(
            description='Destination port to match by numerical value.',
            ge=1,
            le=65535,
            title='Destination Port Number',
        ),
    ] = None
    destinationPortOperator: Annotated[
        Optional[Literal['Equals', 'GreaterOrEquals', 'LessOrEquals']],
        Field(
            description='Operator to use when matching destinationPort, either Equals, GreaterOrEquals, or LessOrEquals.',
            title='Destination Port Operator',
        ),
    ] = None
    destinationPortRange: Annotated[
        Optional[str],
        Field(
            description='Range of destination ports to match, in the format n-m, e.g. 100-200,  The start and end of the range must be port numbers.',
            title='Destination Port Range',
        ),
    ] = None
    destinationPrefix: Annotated[
        Optional[str],
        Field(description='Destination prefix to match.', title='Destination Prefix'),
    ] = None
    firstFragment: Annotated[
        Optional[bool],
        Field(description='Match the first fragment only.', title='First Fragment'),
    ] = None
    fragment: Annotated[
        Optional[bool], Field(description='Match any fragment.', title='Fragment')
    ] = None
    icmpCode: Annotated[
        Optional[List[int]],
        Field(
            description='Match a specific ICMP code, as a number between 0-255, e.g. 0.',
            max_length=255,
            min_length=0,
            title='ICMP Code',
        ),
    ] = None
    icmpTypeName: Annotated[
        Optional[
            Literal[
                'DestUnreachable',
                'Echo',
                'EchoReply',
                'EchoRequest',
                'McastRtrAdv',
                'McastRtrSolicit',
                'McastRtrTerm',
                'MldDone',
                'MldQuery',
                'MldReport',
                'MldV2',
                'NeighborAdvertise',
                'NeighborSolicit',
                'NodeInfoQuery',
                'NodeInfoResponse',
                'PacketTooBig',
                'ParamProblem',
                'Redirect',
                'RouterAdvertise',
                'RouterRenumber',
                'RouterSolicit',
                'SourceQuench',
                'TimeExceeded',
                'Timestamp',
                'TimestampReply',
            ]
        ],
        Field(
            description='Match a specific ICMP type by name, e.g. dest-unreachable.',
            title='ICMP Type Name',
        ),
    ] = None
    icmpTypeNumber: Annotated[
        Optional[int],
        Field(
            description='Match a specific ICMP type by number.',
            ge=0,
            le=255,
            title='ICMP Type Number',
        ),
    ] = None
    protocolName: Annotated[
        Optional[
            Literal[
                'AH',
                'EGP',
                'EIGRP',
                'ESP',
                'GGP',
                'GRE',
                'ICMP',
                'ICMP6',
                'IDRP',
                'IGMP',
                'IGP',
                'IPV4',
                'IPV6',
                'IPV6-DEST-OPTS',
                'IPV6-HOP',
                'L2TP',
                'MPLS-IN-IP',
                'NO-NEXT-HDR',
                'OSPF',
                'PIM',
                'ROHC',
                'RSVP',
                'SCTP',
                'ST',
                'TCP',
                'UDP',
                'VRRP',
            ]
        ],
        Field(
            description='Match a specific IP protocol name (specified in the type field of the IP header).',
            title='Protocol Name',
        ),
    ] = None
    protocolNumber: Annotated[
        Optional[int],
        Field(
            description='Match a specific IP protocol number (specified in the type field of the IP header).',
            ge=0,
            le=255,
            title='Protocol Number',
        ),
    ] = None
    rateLimit: Annotated[
        Optional[RateLimit],
        Field(
            description="Rate limit to apply when the action is 'RateLimit'.",
            title='Rate Limit',
        ),
    ] = None
    sourcePortName: Annotated[
        Optional[
            Literal[
                'ACAP',
                'AFP-TCP',
                'ARNS',
                'ASF-RMCP',
                'ASHARE',
                'ATALK-RM',
                'AURP',
                'AUTH',
                'BFD',
                'BFD-ECHO',
                'BFTP',
                'BGMP',
                'BGP',
                'BOOTPC',
                'BOOTPS',
                'CCSO-NS',
                'CHARGEN',
                'CISCO-TDP',
                'CITADEL',
                'CLEARCASE',
                'COMMERCE',
                'COURIER',
                'DAYTIME',
                'DHCP-FAILOVER',
                'DHCPV6-CLIENT',
                'DHCPV6-SERVER',
                'DICOM',
                'DISCARD',
                'DNSIX',
                'DOMAIN',
                'DSP',
                'ECHO',
                'EPP',
                'ESRO',
                'EXEC',
                'FINGER',
                'FTP',
                'FTP-DATA',
                'FTPS',
                'FTPS-DATA',
                'GODI',
                'GOPHER',
                'GTP-C',
                'GTP-PRIME',
                'GTP-U',
                'HA-CLUSTER',
                'HOSTNAME',
                'HP-ALARM-MGR',
                'HTTP',
                'HTTP-ALT',
                'HTTP-MGMT',
                'HTTP-RPC',
                'HTTPS',
                'IEEE-MMS-SSL',
                'IMAP',
                'IMAP3',
                'IMAPS',
                'IPP',
                'IPSEC',
                'IPX',
                'IRC',
                'IRIS-BEEP',
                'ISAKMP',
                'ISAKMP-NAT',
                'ISCSI',
                'ISO-TSAP',
                'KERBEROS',
                'KERBEROS-ADM',
                'KLOGIN',
                'KPASSWD',
                'KSHELL',
                'L2TP',
                'LDAP',
                'LDAPS',
                'LDP',
                'LMP',
                'LOGIN',
                'LPD',
                'LSP-PING',
                'MAC-SERVER-ADM',
                'MATIP-A',
                'MATIP-B',
                'MICRO-BFD',
                'MICROSOFT-DS',
                'MOBILE-IP',
                'MONITOR',
                'MPP',
                'MS-EXCHANGE',
                'MSDP',
                'MSP',
                'MSSQL-M',
                'MSSQL-S',
                'MULTIHOP-BFD',
                'NAS',
                'NCP',
                'NETBIOS-DATA',
                'NETBIOS-NS',
                'NETBIOS-SS',
                'NETNEWS',
                'NETRJS-1',
                'NETRJS-2',
                'NETRJS-3',
                'NETRJS-4',
                'NETWALL',
                'NEW-RWHO',
                'NFS',
                'NNTP',
                'NNTPS',
                'NTP',
                'ODMR',
                'OLSR',
                'OPENVPN',
                'PIM-AUTO-RP',
                'PKIX-TIMESTAMP',
                'POP2',
                'POP3',
                'POP3S',
                'PPTP',
                'PRINT-SRV',
                'PTP-EVENT',
                'PTP-GENERAL',
                'QMTP',
                'QOTD',
                'RADIUS',
            ]
        ],
        Field(description='Source port to match by name.', title='Source Port Name'),
    ] = None
    sourcePortNumber: Annotated[
        Optional[int],
        Field(
            description='Source port to match by numerical value.',
            ge=1,
            le=65535,
            title='Source Port Number',
        ),
    ] = None
    sourcePortOperator: Annotated[
        Optional[Literal['Equals', 'GreaterOrEquals', 'LessOrEquals']],
        Field(
            description='Operator to use when matching sourcePort, either Equals, GreaterOrEquals, or LessOrEquals.',
            title='Source Port Operator',
        ),
    ] = None
    sourcePortRange: Annotated[
        Optional[str],
        Field(
            description='Range of source ports to match, in the format n-m, e.g. 100-200.  The start and end of the range must be port numbers.',
            title='Source Port Range',
        ),
    ] = None
    sourcePrefix: Annotated[
        Optional[str],
        Field(description='Source prefix to match.', title='Source Prefix'),
    ] = None
    tcpFlags: Annotated[
        Optional[str],
        Field(
            description='Match TCP flags, usable with !, &, | and the flags RST, SYN, and ACK.',
            title='TCP Flags',
        ),
    ] = None


class Entry(BaseModel):
    ipEntry: Annotated[Optional[IpEntry], Field(title='IP Entry')] = None
    type: Annotated[Literal['IPV4', 'IPV6', 'Auto'], Field(title='Type')]


class Filter(BaseModel):
    entries: Annotated[
        List[Entry],
        Field(
            description='Specifies the list of filter entries, in order.',
            title='Entries',
        ),
    ]


class Subinterface(BaseModel):
    index: Annotated[
        Optional[int],
        Field(
            description='Index of the sub-interface. This is ignored on a node running SROS.',
            title='Subinterface Index',
        ),
    ] = None
    interfaceName: Annotated[
        str,
        Field(
            description='Reference to an Interface resource, the combination of the Interface and the specified subinterface index will build the subinterface to be used as a source of traffic to be mirrored. A combination of VLANs, BridgeInterfaces and subinterfaces can be configured as sources together.',
            title='Interface Name',
        ),
    ]
    vlan: Annotated[
        Optional[str],
        Field(
            description='Reference to the VLAN resource under which the sub-interface is configured. This is mandatory when the sub-interface is on a node running SROS and ignored for all other node operating systems.',
            title='VLAN',
        ),
    ] = None


class Subinterfaces(BaseModel):
    bridgeInterfaces: Annotated[
        Optional[List[str]],
        Field(
            description='List of BridgeInterfaces, all traffic from all BridgeInterfaces in the list will be used as sources to be mirrored. A combination of VLANs, BridgeInterfaces and subinterfaces can be configured as sources together.',
            title='Bridge Interfaces',
        ),
    ] = None
    subinterfaces: Annotated[
        Optional[List[Subinterface]],
        Field(
            description='List of Interfaces and subinterface indices',
            title='Subinterfaces',
        ),
    ] = None
    vlans: Annotated[
        Optional[List[str]],
        Field(
            description='List of VLAN resources, all subinterfaces attached to the VLAN will be used as sources to be mirrored.  A combination of VLANs, BridgeInterfaces and subinterfaces can be configured as sources together.',
            title='VLAN',
        ),
    ] = None


class FilterModel(BaseModel):
    filter: Annotated[
        Optional[Filter],
        Field(
            description='Emittes an MirrorFilter and uses the filter as a source for the Mirror.',
            title='Filter',
        ),
    ] = None
    subinterfaces: Annotated[
        Optional[Subinterfaces],
        Field(
            description='Subinterfaces on which to deploy the IPFilter to use as a source for the Mirror.',
            title='Subinterfaces',
        ),
    ] = None


class Interfaces(BaseModel):
    interfaceSelector: Annotated[
        Optional[List[str]],
        Field(
            description='Select Interfaces using a label selector to be mirrored.  Traffic from the entire Interface will be mirrored for any selected Interfaces.  If both a label selector is used and a list of Interfaces is provided, a combination of all selected and provided interfaces will be mirrored.',
            title='Interface Selector',
        ),
    ] = None
    interfaces: Annotated[
        Optional[List[str]],
        Field(
            description='List of Interfaces to be mirrored.  Traffic from the entire Interface will be mirrored for any selected Interfaces.  If both a label selector is used and a list of Interfaces is provided, a combination of all selected and provided interfaces will be mirrored.',
            title='Interfaces',
        ),
    ] = None


class Sources(BaseModel):
    direction: Annotated[
        Literal['Ingress', 'Egress', 'IngressEgress'],
        Field(
            description='The direction of the traffic being mirrored.',
            title='Direction',
        ),
    ]
    filters: Annotated[Optional[List[FilterModel]], Field(title='Filters')] = None
    interfaces: Annotated[
        Optional[Interfaces],
        Field(
            description='Reference to an Interface resource to be mirrored.  Traffic from the entire Interface will be mirrored for any selected Interfaces.',
            title='Interfaces',
        ),
    ] = None
    subinterfaces: Annotated[Optional[Subinterfaces], Field(title='Subinterfaces')] = (
        None
    )


class Spec(BaseModel):
    localDestination: Annotated[
        Optional[LocalDestination],
        Field(
            description='Local destination for the mirror, there can only be either a remote destination or local destination provisioned for a Mirror.',
            title='Local Destination',
        ),
    ] = None
    remoteDestination: Annotated[
        Optional[RemoteDestination],
        Field(
            description='Remote destination for the mirror, there can only be either a remote destination or local destination provisioned for a Mirror.',
            title='Remote Destination',
        ),
    ] = None
    sources: Annotated[Sources, Field(description='Mirror sources.', title='Sources')]


class SubinterfaceModel(BaseModel):
    configuredSource: Annotated[
        Literal[
            'VLAN',
            'BridgeInterface',
            'Subinterface',
            'Interface',
            'FilterV4',
            'FilterV6',
        ],
        Field(
            description='Indicates what is driving the particular subinterface to be selected as a mirror source.',
            title='Configured Source',
        ),
    ]
    interface: Annotated[
        str, Field(description='Node specific interface name.', title='Interface')
    ]
    node: Annotated[str, Field(description='Reference to Node object.', title='Node')]
    operatingSystem: Annotated[
        str,
        Field(description='Operating System of the Node.', title='Operating System'),
    ]
    subinterfaceIndex: Annotated[
        Optional[int],
        Field(
            description='Index allocated to the subinterface which is being mirrored. If an interface is used as a source, this will not be set.',
            title='Subinterface Index',
        ),
    ] = None
    vlanID: Annotated[
        Optional[str],
        Field(description='vlan assigned to this subinterface.', title='VLAN ID'),
    ] = None


class Status(BaseModel):
    lastChange: Annotated[
        Optional[date],
        Field(
            description='Indicates when this SubInterface last changed state.',
            title='Last Change',
        ),
    ] = None
    mirrorID: Annotated[
        Optional[str],
        Field(
            description='Mirror Identifier used as the name of the mirror.',
            title='MirrorID',
        ),
    ] = None
    numActiveInterfaces: Annotated[
        Optional[int],
        Field(
            description='Total number of active Interfaces used as sources of the mirror.',
            title='Number of Active Interfaces',
        ),
    ] = None
    numActiveSubinterfaces: Annotated[
        Optional[int],
        Field(
            description='Total number of active subinterfaces used as sources of the mirror.',
            title='Number of Active Subinterfaces',
        ),
    ] = None
    numActiveV4FilterSubinterfaces: Annotated[
        Optional[int],
        Field(
            description='Total number of active subinterfaces used as sources of the mirror derived from IPV4Filter associations.',
            title='Number of Active V4 Filter Subinterfaces',
        ),
    ] = None
    numActiveV6FilterSubinterfaces: Annotated[
        Optional[int],
        Field(
            description='Total number of active subinterfaces used as sources of the mirror derived from IPV6Filter associations.',
            title='Number of Active V6 Filter Subinterfaces',
        ),
    ] = None
    numActiveVLANSubinterfaces: Annotated[
        Optional[int],
        Field(
            description='Total number of active subinterfaces used as sources of the mirror derived from VLAN resource references.',
            title='Number of Active VLAN Subinterfaces',
        ),
    ] = None
    numberActiveBridgeInterfaces: Annotated[
        Optional[int],
        Field(
            description='Total number of active subinterfaces used as sources of the mirror derived from BridgeInterface resource references.',
            title='Number of Active Bridge Interfaces',
        ),
    ] = None
    operationalState: Annotated[
        Optional[str],
        Field(
            description='Indicates the current operational state of the Mirror instance.',
            title='Operational State',
        ),
    ] = None
    subinterfaces: Annotated[
        Optional[List[SubinterfaceModel]],
        Field(description='List of members in this Interface.', title='Subinterfaces'),
    ] = None


class Mirror(BaseModel):
    apiVersion: str
    kind: str
    metadata: Metadata
    spec: Annotated[
        Spec,
        Field(
            description='Mirror allows for the configuration of mirroring sources, including interfaces, subinterfaces, and filters, as well as the destination for the mirrored traffic, which can be either local or remote.',
            title='Specification',
        ),
    ]
    status: Annotated[
        Optional[Status],
        Field(
            description='MirrorStatus defines the observed state of Mirror',
            title='Status',
        ),
    ] = None


class MirrorList(BaseModel):
    apiVersion: str
    items: Optional[List[Mirror]] = None
    kind: str
