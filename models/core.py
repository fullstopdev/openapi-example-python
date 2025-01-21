# generated by datamodel-codegen:
#   filename:  core.json
#   timestamp: 2025-01-21T07:52:25+00:00

from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List, Literal, Optional

from pydantic import BaseModel, Field, RootModel
from typing_extensions import Annotated


class AlarmData(BaseModel):
    acknowledged: Annotated[
        Optional[bool],
        Field(description='An indication if the alarm has been acknowledged.'),
    ] = None
    cleared: Annotated[
        Optional[bool],
        Field(description='An indication if the alarm has been cleared.'),
    ] = None
    clusterMember: Annotated[
        Optional[str],
        Field(description='The cluster member that generated this alarm.'),
    ] = None
    description: Annotated[
        Optional[str], Field(description='A description for the alarm.')
    ] = None
    group: Annotated[
        Optional[str],
        Field(
            description='Indicates the group of the resource the alarm is present on.'
        ),
    ] = None
    jsPath: Annotated[
        Optional[str],
        Field(
            description='a unnormalized jspath relating to the object in the alarm state. For\nexample\n.node{.name=="spine-1-1"}.srl{.version=="24.10.1"}.interface{.name=="ethernet-1-1"}.'
        ),
    ] = None
    kind: Annotated[
        Optional[str],
        Field(description='Indicates the kind of resource the alarm is present on.'),
    ] = None
    lastAcknowledged: Annotated[
        Optional[str], Field(description='the time this alarm was last acknowledged.')
    ] = None
    lastChanged: Annotated[
        Optional[str],
        Field(
            description='The last time that the alarm was changed; as provided by the raiser of the alarm.'
        ),
    ] = None
    name: Annotated[
        Optional[str],
        Field(
            description='The unique name for the alarm, e.g. InterfaceDown-spine-1-1-ethernet-1-1.'
        ),
    ] = None
    namespace: Annotated[
        Optional[str], Field(description='The namespace of the alarm')
    ] = None
    occurrences: Annotated[
        Optional[int],
        Field(
            description='The number of occurrences of this alarm (the number of times it has been raised).'
        ),
    ] = None
    parentAlarm: Annotated[
        Optional[str],
        Field(
            description='a name of another alarm that is a parent of this alarm. This is used to\nfilter out alarms that are not a root cause.'
        ),
    ] = None
    probableCause: Annotated[
        Optional[str],
        Field(
            description='the probable cause for raising the alarm. This field is optional, and\nshould also be a description indicating the primary probable cause of the\nalarm, which may be enriched with relevant information from this specific\nalarm instance. The complete alarm below contains an example.'
        ),
    ] = None
    remedialAction: Annotated[
        Optional[str],
        Field(
            description='any remedial actions the user could try to resolve/clear the alarm. This\nfield is optional, and may also be enriched with relevant information\nfrom this specific alarm instance. The complete alarm below contains an\nexample.'
        ),
    ] = None
    resource: Annotated[
        Optional[str],
        Field(description='The name of the resource that this alarm is present on.'),
    ] = None
    severity: Annotated[
        Optional[Literal['warning', ' minor', ' major', ' critical']],
        Field(description='Severity of the alarm'),
    ] = None
    sourceGroup: Annotated[
        Optional[str],
        Field(
            description='Indicates indicates the group of the resource that raised this alarm, e.g. interfaces.eda.nokia.com.'
        ),
    ] = None
    sourceKind: Annotated[
        Optional[str],
        Field(
            description='Indicates the Kind of the resource that raised this alarm, e.g. InterfaceState.'
        ),
    ] = None
    sourceResource: Annotated[
        Optional[str],
        Field(
            description='Indicates the the name of the resource that raised this alarm, e.g. spine-1-1-ethernet-1-1.'
        ),
    ] = None
    suppressed: Annotated[
        Optional[bool],
        Field(description='An indication if the alarm has been suppressed.'),
    ] = None
    suppressedUntil: Annotated[
        Optional[str],
        Field(
            description='Indicates the time at which an active instance of the alarm will be raised again.'
        ),
    ] = None
    type: Annotated[
        Optional[str], Field(description='A kind for the alarm, e.g. InterfaceDown')
    ] = None


class AlarmHistoryData(BaseModel):
    alarm: Optional[AlarmData] = None
    index: Annotated[
        Optional[str],
        Field(
            description='The index of the history entry within the entries for a single alarm..'
        ),
    ] = None


class AlarmNamespaceAndName(BaseModel):
    name: Annotated[Optional[str], Field(description='The name of an alarm')] = None
    namespace: Annotated[
        Optional[str], Field(description='The namespace of an alarm')
    ] = None


class AuthPasswordPolicy(BaseModel):
    allowUserName: Annotated[
        Optional[bool],
        Field(
            description='If true, prevents passwords from being or containing the user name.'
        ),
    ] = None
    digits: Annotated[
        Optional[int],
        Field(
            description='Minimum number of digits required in a password. Can be zero.'
        ),
    ] = None
    forceExpiredPasswordChange: Annotated[
        Optional[int],
        Field(
            description='The maximum number of days until a password change is enforced.\nA value of zero means no change is required.'
        ),
    ] = None
    hashingAlgorithm: Annotated[
        Optional[Literal['argon2', 'pbkdf2-sha512', 'pbkdf2-sha256', 'pbkdf2']],
        Field(
            description='The hashing algorithm to use when hashing stored passwords.'
        ),
    ] = None
    length: Annotated[
        Optional[int],
        Field(description='Minimum password length.  This must be at least 1.'),
    ] = None
    lowerCase: Annotated[
        Optional[int],
        Field(
            description='Minimum number of lower case characters required in a password. Can be zero.'
        ),
    ] = None
    maxFailureWaitSeconds: Annotated[
        Optional[int],
        Field(
            description='The number of seconds before the users access will be restored, after too many authentication failures.'
        ),
    ] = None
    maxLoginFailure: Annotated[
        Optional[int],
        Field(
            description='The number of login/authentication failures before a lockout policy takes effect. Zero means no enforcement.'
        ),
    ] = None
    passwordHistory: Annotated[
        Optional[int],
        Field(
            description='The number of passwords remembered to enforce no re-use of passwords. Zero means no re-use enforcement.'
        ),
    ] = None
    permanentLockout: Annotated[
        Optional[bool],
        Field(
            description='If true, lockout is permanent and the users access must be re-enabled by an administrator.\nIf false, the users access will be re-enabled after "maxFailureWaitSeconds" seconds.'
        ),
    ] = None
    resetTimeSeconds: Annotated[
        Optional[int],
        Field(
            description='When lockout is not permanent, the count of authentication failures for a user will be reset\nthis many seconds after the last authentication failure.'
        ),
    ] = None
    specialChars: Annotated[
        Optional[int],
        Field(
            description='Minimum number of special characters required in a password. Can be zero.'
        ),
    ] = None
    upperCase: Annotated[
        Optional[int],
        Field(
            description='Minimum number of upper case characters required in a password. Can be zero.'
        ),
    ] = None


class Credentials(BaseModel):
    temporary: Annotated[
        Optional[bool],
        Field(
            description='This is true if the password being set is a temporary password.  In this case the user\nis required to change the password after they login using the temporary password.'
        ),
    ] = None
    value: Annotated[
        Optional[str], Field(description='The new password for the user.')
    ] = None


class ErrorIndex(BaseModel):
    index: Optional[int] = None


class ErrorItem(BaseModel):
    error: Optional[Dict[str, Any]] = None
    type: Optional[str] = None


class ErrorResponse(BaseModel):
    code: Annotated[
        int, Field(description='the numeric HTTP error code for the response.')
    ]
    details: Annotated[
        Optional[str], Field(description='The optional details of the error response.')
    ] = None
    dictionary: Annotated[
        Optional[Dict[str, Dict[str, Any]]],
        Field(
            description='Dictionary/map of associated data/information relevant to the error.\nThe error "message" may contain {{name}} escapes that should be substituted\nwith information from this dictionary.'
        ),
    ] = None
    errors: Annotated[
        Optional[List[ErrorItem]],
        Field(
            description='Collection of errors in cases where more than one exists. This needs to be\nflexible so we can support multiple formats'
        ),
    ] = None
    index: Optional[ErrorIndex] = None
    internal: Annotated[
        Optional[int],
        Field(
            description="Internal error code in cases where we don't have an array of errors"
        ),
    ] = None
    message: Annotated[
        str, Field(description='The basic text error message for the error response.')
    ]
    ref: Annotated[
        Optional[str],
        Field(
            description='Reference to the error source. Should typically be the URI of the request'
        ),
    ] = None
    type: Annotated[
        Optional[str],
        Field(
            description='URI pointing at a document that describes the error and mitigation steps\nIf there is no document, point to the RFC for the HTTP error code'
        ),
    ] = None


class GroupIDs(RootModel[List[str]]):
    root: Annotated[
        List[str], Field(title='A list of user group identifiers (uuid values).')
    ]


class GroupProviderConfig(BaseModel):
    NameLDAPAttribute: Annotated[
        Optional[str], Field(description='The LDAP group name attribute')
    ] = None
    filter: Annotated[
        Optional[str],
        Field(
            description='Further for filtering when retrieving LDAP groups. Ensure starts and ends with parentheses if using.'
        ),
    ] = None
    groupLDAPDN: Annotated[
        Optional[str], Field(description='The LDAP DN where groups are found.')
    ] = None
    memberAttribute: Annotated[
        Optional[str],
        Field(
            description='The group attribute for a members.  usually "member" or "memberUid".'
        ),
    ] = None
    memberOfAttribute: Annotated[
        Optional[str],
        Field(
            description='If strategy is "memberOf", this is the user attribute for group memberships.'
        ),
    ] = None
    membershipAttributeType: Annotated[
        Optional[str],
        Field(
            description='How users are identified in a group member entry: either DN or UID.'
        ),
    ] = None
    membershipUserAttribute: Annotated[
        Optional[str],
        Field(
            description='Only valid if membershipAttributeType is UID; then it is\nthe user attribute that should match the group member value.'
        ),
    ] = None
    objectClasses: Annotated[
        Optional[str],
        Field(
            description='The LDAP object class or classes es used for groups. If more than one, must be comma separated.'
        ),
    ] = None
    retrievalStrategy: Annotated[
        Optional[str],
        Field(
            description='The strategy for retrieving groups.  "member" to get group membership from the group, ObjectNameParam\n"memberOf" to get group membership from the user.'
        ),
    ] = None


class GroupVersionKind(BaseModel):
    group: Optional[str] = None
    kind: Optional[str] = None
    version: Optional[str] = None


class HealthServiceStatus(BaseModel):
    error: Annotated[
        Optional[str], Field(description='Detailed status if the service is not up.')
    ] = None
    status: Annotated[
        Literal['UP', 'DOWN'],
        Field(description='Health status of the given service.  UP or DOWN.'),
    ]


class LabelCompletionResponse(BaseModel):
    results: Optional[List[str]] = None


class LineSegment(BaseModel):
    endLine: Optional[int] = None
    startLine: Optional[int] = None


class Metadata(BaseModel):
    annotations: Optional[Dict[str, str]] = None
    labels: Optional[Dict[str, str]] = None
    name: Annotated[
        str,
        Field(
            max_length=253,
            pattern='^[a-z0-9]([-a-z0-9]*[a-z0-9])?(\\.[a-z0-9]([-a-z0-9]*[a-z0-9])?)*$',
        ),
    ]
    namespace: Optional[str] = None


class NsCrGvkName(BaseModel):
    gvk: Optional[GroupVersionKind] = None
    name: Optional[str] = None
    namespace: Optional[str] = None


class ProviderAuth(BaseModel):
    bindCredential: Annotated[
        Optional[str],
        Field(description='Credentials to use when binding to an LDAP provider'),
    ] = None
    bindDN: Annotated[
        Optional[str], Field(description='DN to use when binding to an LDAP provider')
    ] = None


class QueryCompletion(BaseModel):
    completion: Optional[str] = None
    token: Optional[str] = None


class QueryCompletionResponse(BaseModel):
    completions: Annotated[
        Optional[List[QueryCompletion]],
        Field(description='Array of possible auto-completion results.'),
    ] = None


class ResourceRule(BaseModel):
    apiGroups: List[str]
    permissions: Optional[str] = None
    resources: List[str]


class StreamResult(BaseModel):
    details: Annotated[
        Optional[str],
        Field(
            description='The details for the streaming request; e.g. the query string in the corresponding GET request.'
        ),
    ] = None
    stream: Annotated[
        Optional[str],
        Field(
            description='The stream identifier specified in the corresponding streaming GET request.'
        ),
    ] = None


class TableRule(BaseModel):
    path: str
    permissions: str


class TopoAttrMetadata(BaseModel):
    type: Optional[str] = None
    ui_description: Optional[str] = None
    ui_description_key: Optional[str] = None
    ui_name: Optional[str] = None
    ui_name_key: Optional[str] = None


class TopoLinkEndpoint(BaseModel):
    endpoint: Optional[str] = None
    node: Optional[str] = None


class TopoNodeGrouping(BaseModel):
    group: Optional[str] = None
    tier: Optional[int] = None


class TopoOverlayBadgeMetadata(BaseModel):
    badge_name: Optional[str] = None
    badge_path: Optional[str] = None
    color: Optional[str] = None
    ui_description: Optional[str] = None
    ui_description_key: Optional[str] = None
    ui_name: Optional[str] = None
    ui_name_key: Optional[str] = None
    value: Optional[int] = None


class TopoOverlayStateMetadata(BaseModel):
    color: Optional[str] = None
    ui_description: Optional[str] = None
    ui_description_key: Optional[str] = None
    ui_name: Optional[str] = None
    ui_name_key: Optional[str] = None
    value: Optional[int] = None


class TopoOverlayStateRequest(BaseModel):
    badge: Optional[str] = None
    status: Optional[str] = None


class TopoSchema(BaseModel):
    group: Optional[str] = None
    kind: Optional[str] = None
    version: Optional[str] = None


class TopologyStateGroupSelector(BaseModel):
    group: Annotated[
        Optional[str],
        Field(
            description='The group to assign to nodes that match the selector.\n+eda:ui:title="Group"'
        ),
    ] = None
    nodeSelector: Annotated[
        Optional[List[str]],
        Field(
            description='+kubebuilder:validation:Optional\n+eda:ui:title="Node Selector"\n+eda:ui:format="labelselector"\nLabel selector to use to match nodes that should be assigned to this group.'
        ),
    ] = None


class TopologyStateTierSelector(BaseModel):
    nodeSelector: Annotated[
        Optional[List[str]],
        Field(
            description='+kubebuilder:validation:Optional\n+eda:ui:title="Node Selector"\n+eda:ui:format="labelselector"\nLabel selector to use to match nodes that should be assigned to this tier.'
        ),
    ] = None
    tier: Annotated[
        Optional[int],
        Field(
            description='The tier to assign to nodes that match the selector.\n+eda:ui:title="Tier"'
        ),
    ] = None


class TransactionContent(BaseModel):
    apiVersion: Optional[str] = None
    kind: Optional[str] = None
    metadata: Optional[Metadata] = None
    spec: Optional[Dict[str, Any]] = None


class TransactionId(BaseModel):
    id: Annotated[
        Optional[int],
        Field(
            description='A transaction identifier; these are assigned by the system to a posted transaction.'
        ),
    ] = None


class TransactionInputCr(BaseModel):
    isDelete: Optional[bool] = None
    name: Optional[NsCrGvkName] = None


class TransactionNodeResult(BaseModel):
    errors: Annotated[
        Optional[List[str]], Field(description='Resulting errors for the node')
    ] = None
    name: Annotated[Optional[str], Field(description='The name of the node')] = None
    namespace: Annotated[
        Optional[str], Field(description='The namespace of the node')
    ] = None


class TransactionNsCrGvkNames(BaseModel):
    gvk: Optional[GroupVersionKind] = None
    names: Optional[List[str]] = None
    namespace: Optional[str] = None


class TransactionPoolAllocation(BaseModel):
    key: Optional[str] = None
    poolName: Optional[str] = None
    poolTemplate: Optional[str] = None
    value: Optional[str] = None


class TransactionResultObjectString(BaseModel):
    data: Optional[str] = None


class TransactionScriptResults(BaseModel):
    executionTime: Optional[int] = None
    output: Optional[str] = None


class TransactionState(BaseModel):
    state: Annotated[
        Optional[str], Field(description='The state of the transaction')
    ] = None


class TransactionStructuredAppError(BaseModel):
    message: Optional[str] = None
    messageKey: Optional[str] = None
    values: Optional[Dict[str, Dict[str, Any]]] = None


class TransactionSummaryResult(BaseModel):
    commitHash: Annotated[
        Optional[str], Field(description='The git commit hash for the transaction')
    ] = None
    description: Annotated[
        Optional[str],
        Field(
            description='The description of the transaction, as posted in the transaction request.'
        ),
    ] = None
    details: Annotated[
        Optional[str],
        Field(
            description='The type of details available for the transaction, as posted in the transaction request.'
        ),
    ] = None
    dryRun: Annotated[
        Optional[bool],
        Field(
            description='If true the transaction was not committed and ran in dry run mode.'
        ),
    ] = None
    id: Annotated[Optional[int], Field(description='The transaction identifier')] = None
    lastChangeTimestamp: Annotated[
        Optional[str], Field(description='The time that the transaction completed.')
    ] = None
    state: Annotated[
        Optional[str], Field(description='The state of the transaction.')
    ] = None
    success: Annotated[
        Optional[bool], Field(description='True if the transaction was successful.')
    ] = None
    username: Annotated[
        Optional[str], Field(description='The user who posted the transaction.')
    ] = None


class TransactionSummaryResults(BaseModel):
    results: Annotated[
        Optional[List[TransactionSummaryResult]],
        Field(description='array of summary-results for transactions'),
    ] = None


class TransactionValue(BaseModel):
    value: Optional[TransactionContent] = None


class UrlRule(BaseModel):
    path: str
    permissions: Optional[str] = None


class UserStatus(BaseModel):
    failedLoginSinceSuccessfulLogin: Optional[int] = None
    lastFailedLogin: Optional[str] = None
    lastSuccessfulLogin: Optional[str] = None
    temporarilyDisabled: Optional[bool] = None


class UserStorageInFileContent(BaseModel):
    file_content: Annotated[
        str,
        Field(
            alias='file-content',
            description='The desired content of the user-storage file. This will be base64 decoded before storing if the request indicates that the content is base64 encoded.',
        ),
    ]


class UserStorageOutDirEntry(BaseModel):
    modification_time: Annotated[
        Optional[datetime],
        Field(
            alias='modification-time',
            description='modification type of the item, if a file',
        ),
    ] = None
    name: Annotated[str, Field(description='name of the item within the directory')]
    type: Annotated[str, Field(description='type of the item; "file" or "directory"')]


class UserStorageOutFileContent(BaseModel):
    file_content: Annotated[
        Optional[str],
        Field(
            alias='file-content',
            description='content of the file, will be base64 encoded if the request asked for this',
        ),
    ] = None
    file_deleted: Annotated[
        Optional[bool],
        Field(
            alias='file-deleted',
            description='if present and true, indicates the file has been deleted; used for\nstreamed responses',
        ),
    ] = None
    file_name: Annotated[str, Field(alias='file-name', description='name of the file')]
    modification_time: Annotated[
        Optional[datetime],
        Field(
            alias='modification-time',
            description='UTC modification time of the file, as an RFC 3339 date/time.\nNot valid if file-deleted is true (in a streamed response)',
        ),
    ] = None


class Workflow(BaseModel):
    cr: Annotated[
        Dict[str, Dict[str, Any]],
        Field(description='Custom resource that defines the workflow to execute'),
    ]
    description: Annotated[
        str, Field(description='Description message for the workflow')
    ]


class WorkflowId(BaseModel):
    id: Annotated[
        Optional[int],
        Field(
            description='A workflow identifier; these are assigned by the system to a posted workflow.'
        ),
    ] = None


class WorkflowState(BaseModel):
    runningState: Optional[str] = None
    state: Optional[str] = None


class SingleVersionInfo(BaseModel):
    builtDate: Annotated[
        Optional[str], Field(description='The build-time for the component.')
    ] = None
    version: Annotated[
        Optional[str], Field(description='The version string for the component.')
    ] = None


class VersionInfo(RootModel[Optional[Dict[str, SingleVersionInfo]]]):
    root: Optional[Dict[str, SingleVersionInfo]] = None


class AuthProvider(BaseModel):
    auth: Optional[ProviderAuth] = None
    enabled: Annotated[
        Optional[bool],
        Field(description='If true, checking/syncing this LDAP provider is enabled.'),
    ] = None
    groupSupport: Optional[GroupProviderConfig] = None
    idAttribute: Annotated[
        Optional[str],
        Field(
            description='Name of the LDAP attribute, which is used as a unique object identifier (UUID) for objects in LDAP.'
        ),
    ] = None
    import_: Annotated[
        Optional[bool],
        Field(
            alias='import',
            description='If true, the LDAP information will be imported into the EDA (Keycloak) database.',
        ),
    ] = None
    name: Annotated[
        Optional[str],
        Field(description='The name to give to the LDAP provider; must be unique.'),
    ] = None
    pagination: Annotated[
        Optional[bool],
        Field(description='Set to true if the LDAP server supports pagination.'),
    ] = None
    periodicSync: Annotated[
        Optional[bool],
        Field(
            description='If true, periodic synchronization of new changed or newly created LDAP users to Keycloak will occur.'
        ),
    ] = None
    periodicSyncSecs: Annotated[
        Optional[int],
        Field(
            description='If periodic sync is enabled, this is the period in seconds that synchronization will occur.'
        ),
    ] = None
    rdnLDAPAttribute: Annotated[
        Optional[str],
        Field(
            description="Name of the LDAP attribute, which is used as RDN (top attribute) of typical user DN. Usually it's the same as the Username LDAP attribute, however it is not required."
        ),
    ] = None
    readOnly: Annotated[
        Optional[bool],
        Field(
            description='If true, changes made to LDAP-mapped attribute via EDA will be synced back to the LDAP server.  Otherwise, changes are not made in LDAP.'
        ),
    ] = None
    scope: Annotated[
        Optional[str],
        Field(
            description='Must be "One Level" or "Subtree".  If "One Level", the search applies only for users in the DNs specified by User DNs. If "Subtree", the search applies to the whole subtree.'
        ),
    ] = None
    timeout: Annotated[
        Optional[int], Field(description='LDAP connection timeout in milliseconds')
    ] = None
    tls: Annotated[
        Optional[bool],
        Field(description='If true, encrypts the connection to LDAP using STARTTLS'),
    ] = None
    url: Annotated[
        Optional[str], Field(description='Connection URL to your LDAP server')
    ] = None
    userDN: Annotated[
        Optional[str],
        Field(
            description='Full DN of LDAP tree where your users are. This DN is the parent of LDAP users.'
        ),
    ] = None
    userObjectClasses: Annotated[
        Optional[str], Field(examples=["'inetOrgPerson, organizationalPerson'."])
    ] = None
    userSearchFilter: Annotated[
        Optional[str],
        Field(
            description="Additional LDAP filter for filtering searched users. Leave this empty if you don't need an additional filter. Make sure that it starts with '(' and ends with ')'."
        ),
    ] = None
    usernameAttribute: Annotated[
        Optional[str],
        Field(
            description="Name of the LDAP attribute, which is mapped as EDA username. For many LDAP server vendors it can be 'uid'."
        ),
    ] = None
    uuid: Annotated[
        Optional[str],
        Field(
            description='The unique identifier given to the entry when it is created.'
        ),
    ] = None
    vendor: Annotated[Optional[str], Field(description='LDAP vendor (provider).')] = (
        None
    )


class AuthProviders(RootModel[List[AuthProvider]]):
    root: List[AuthProvider]


class AuthRole(BaseModel):
    description: str
    name: Annotated[
        str,
        Field(
            pattern='^[a-z0-9]([-a-z0-9]*[a-z0-9])?(\\.[a-z0-9]([-a-z0-9]*[a-z0-9])?)*$'
        ),
    ]
    namespace: Annotated[
        Optional[str], Field(pattern='^([a-z0-9]([-a-z0-9]*[a-z0-9])?)?$')
    ] = None
    resourceRules: Optional[List[ResourceRule]] = None
    tableRules: Optional[List[TableRule]] = None
    urlRules: Optional[List[UrlRule]] = None


class AuthRoles(RootModel[List[AuthRole]]):
    root: List[AuthRole]


class AuthUser(BaseModel):
    email: Optional[str] = None
    enabled: Optional[bool] = None
    firstName: Optional[str] = None
    groups: Annotated[
        Optional[List[str]],
        Field(
            description='contains the UUIDs of the groups of which the user is a member.'
        ),
    ] = None
    lastName: Optional[str] = None
    maxSessions: Optional[int] = None
    password: Optional[str] = None
    status: Optional[UserStatus] = None
    username: Optional[str] = None
    uuid: Optional[str] = None


class AuthUserGroup(BaseModel):
    description: Optional[str] = None
    full_users: Annotated[
        Optional[List[AuthUser]],
        Field(
            alias='full-users',
            description='contains the full user definitions of the users who are members of the group, if requested',
        ),
    ] = None
    fullRoles: Annotated[
        Optional[List[AuthRole]],
        Field(
            description='contains the full role definitions of the Roles and ClusterRoles associated with the group, if requested'
        ),
    ] = None
    name: Optional[str] = None
    roles: Annotated[
        Optional[List[str]],
        Field(
            description='Contains the names of the ClusterRoles and Roles roles associated with the group.\nA Role name has the form "namesspace:rolename", whereas a ClusteRole name is a\nsimple "rolename", without a colon or a namespace.'
        ),
    ] = None
    users: Annotated[
        Optional[List[str]],
        Field(
            description='contains the usernames of the users who are members of the group'
        ),
    ] = None
    uuid: Optional[str] = None


class AuthUserGroups(RootModel[List[AuthUserGroup]]):
    root: List[AuthUserGroup]


class AuthUsers(RootModel[List[AuthUser]]):
    root: List[AuthUser]


class CrAnnotation(BaseModel):
    cr: Optional[NsCrGvkName] = None
    lines: Optional[List[LineSegment]] = None


class GetLabelCompletionRequest(BaseModel):
    gvk: GroupVersionKind
    limit: Annotated[
        Optional[int], Field(description='The maximum number of results to return')
    ] = None
    namespace: Annotated[
        Optional[str],
        Field(
            description='The namespace of the GVK if the CRD is namespaced\nrequired: true if the GVK is namespaced'
        ),
    ] = None
    value: Annotated[
        str,
        Field(
            description='A key value string delimited by =.  If the Value does not include an =\nit is assumed to be a Key lookup.  If there is an =, everything before\nthe = is assumed to be the key and the lookup will be a value lookup'
        ),
    ]


class Health(BaseModel):
    mode: Annotated[
        Literal['ACTIVE', 'STANDBY'],
        Field(description='Indication of the activity of this cluster.'),
    ]
    services: Annotated[
        Optional[Dict[str, HealthServiceStatus]],
        Field(
            description='Detailed health of the services comprising the EDA cluster.  Keyed by the name of the service.'
        ),
    ] = None
    status: Annotated[
        Literal['UP', 'DEGRADED', 'DOWN'],
        Field(description='Overall health status of the EDA cluster.'),
    ]
    timestamp: Annotated[
        datetime, Field(description='Time that the health report was generated.')
    ]


class NodeConfigResponse(BaseModel):
    annotations: Annotated[
        Optional[List[CrAnnotation]],
        Field(description='The the list of annotations for the node configuration'),
    ] = None
    running: Annotated[
        Optional[str], Field(description='The current node configuration for the node')
    ] = None


class Overlay(BaseModel):
    endpoint_state: Optional[List[TopoOverlayStateMetadata]] = None
    group: Optional[str] = None
    link_state: Optional[List[TopoOverlayStateMetadata]] = None
    name: Optional[str] = None
    node_badge: Optional[List[TopoOverlayBadgeMetadata]] = None
    node_state: Optional[List[TopoOverlayStateMetadata]] = None
    ui_description: Optional[str] = None
    ui_description_key: Optional[str] = None
    ui_name: Optional[str] = None
    ui_name_key: Optional[str] = None
    version: Optional[str] = None


class Overlays(RootModel[List[Overlay]]):
    root: List[Overlay]


class TopoElemMetadata(BaseModel):
    attributes: Optional[Dict[str, TopoAttrMetadata]] = None
    schema_: Annotated[Optional[TopoSchema], Field(alias='schema')] = None
    subtitle: Optional[str] = None
    subtitle_key: Optional[str] = None


class TopoEndpoint(BaseModel):
    attributes: Optional[Dict[str, Dict[str, Any]]] = None
    cr_name: Optional[str] = None
    labels: Optional[Dict[str, str]] = None
    name: Optional[str] = None
    namespace: Optional[str] = None
    schema_: Annotated[Optional[TopoSchema], Field(alias='schema')] = None
    ui_name: Optional[str] = None


class TopoLink(BaseModel):
    attributes: Optional[Dict[str, Dict[str, Any]]] = None
    cr_name: Optional[str] = None
    endpoint_a: Optional[TopoLinkEndpoint] = None
    endpoint_a_details: Optional[TopoEndpoint] = None
    endpoint_b: Optional[TopoLinkEndpoint] = None
    endpoint_b_details: Optional[TopoEndpoint] = None
    labels: Optional[Dict[str, str]] = None
    name: Optional[str] = None
    namespace: Optional[str] = None
    schema_: Annotated[Optional[TopoSchema], Field(alias='schema')] = None
    ui_name: Optional[str] = None


class TopoNode(BaseModel):
    attributes: Optional[Dict[str, Dict[str, Any]]] = None
    cr_name: Optional[str] = None
    grouping: Optional[TopoNodeGrouping] = None
    labels: Optional[Dict[str, str]] = None
    name: Optional[str] = None
    namespace: Optional[str] = None
    schema_: Annotated[Optional[TopoSchema], Field(alias='schema')] = None
    ui_name: Optional[str] = None


class Topology(BaseModel):
    endpoints: Optional[TopoElemMetadata] = None
    group: Optional[str] = None
    grouping: Optional[TopoSchema] = None
    links: Optional[TopoElemMetadata] = None
    name: Optional[str] = None
    nodes: Optional[TopoElemMetadata] = None
    ui_description: Optional[str] = None
    ui_description_key: Optional[str] = None
    ui_name: Optional[str] = None
    ui_name_key: Optional[str] = None
    version: Optional[str] = None


class TopologyState(BaseModel):
    links: Optional[Dict[str, TopoLink]] = None
    nodes: Optional[Dict[str, TopoNode]] = None


class TopologyStateGroupingBase(BaseModel):
    groupSelectors: Annotated[
        Optional[List[TopologyStateGroupSelector]],
        Field(
            description='The set of selectors for assigning nodes to groups\n+eda:ui:title="Group Selectors"'
        ),
    ] = None
    tierSelectors: Annotated[
        Optional[List[TopologyStateTierSelector]],
        Field(
            description='The set of selectors for assigning nodes to tiers\n+eda:ui:title="Tier Selectors"'
        ),
    ] = None
    uiDescription: Annotated[
        Optional[str],
        Field(
            description='A description of the topology grouping to expose in the UI\n+eda:ui:title="UI Description"'
        ),
    ] = None
    uiDescriptionKey: Annotated[
        Optional[str],
        Field(
            description='The translation key for the description of the topology grouping to expose in the UI\n+eda:ui:title="UI Description Key"'
        ),
    ] = None
    uiName: Annotated[
        Optional[str],
        Field(
            description='The name of the topology grouping to expose in the UI\n+eda:ui:title="UI Name"'
        ),
    ] = None
    uiNameKey: Annotated[
        Optional[str],
        Field(
            description='The translation key for the name of the topology grouping to expose in the UI\n+eda:ui:title="UI Name Key"'
        ),
    ] = None


class TransactionAppError(BaseModel):
    rawError: Optional[str] = None
    structuredError: Optional[TransactionStructuredAppError] = None


class TransactionIntentResult(BaseModel):
    errors: Optional[List[TransactionAppError]] = None
    intentName: Optional[NsCrGvkName] = None
    outputCrs: Optional[List[NsCrGvkName]] = None
    poolAllocation: Optional[List[TransactionPoolAllocation]] = None
    script: Optional[TransactionScriptResults] = None


class TransactionResultObject(BaseModel):
    after: Optional[TransactionResultObjectString] = None
    before: Optional[TransactionResultObjectString] = None
    dataUnavailable: Annotated[
        Optional[bool],
        Field(description='True if there is no data available for the result'),
    ] = None
    format: Annotated[
        Optional[str], Field(description='The format of the response - Text or YAML')
    ] = None


class TransactionType(BaseModel):
    create: Optional[TransactionValue] = None
    delete: Optional[NsCrGvkName] = None
    modify: Optional[TransactionValue] = None
    replace: Optional[TransactionValue] = None


class UserStorageOutDirContent(BaseModel):
    directory_path: Annotated[
        str,
        Field(
            alias='directory-path',
            description='path for the directory within the users storage',
        ),
    ]
    entries: Annotated[
        List[UserStorageOutDirEntry],
        Field(description='array of entries for the items in the directory'),
    ]


class WorkflowResult(BaseModel):
    errorMessage: Optional[str] = None
    resultMessage: Optional[str] = None
    state: Optional[WorkflowState] = None
    success: Optional[bool] = None


class TopoGroupingStateRequest(BaseModel):
    name: Optional[str] = None
    spec: Optional[TopologyStateGroupingBase] = None


class TopoStateRequest(BaseModel):
    grouping: Optional[TopoGroupingStateRequest] = None
    namespace: Optional[str] = None
    overlays: Optional[TopoOverlayStateRequest] = None


class Topologies(RootModel[List[Topology]]):
    root: List[Topology]


class TransactionCr(BaseModel):
    type: Optional[TransactionType] = None


class TransactionDetails(BaseModel):
    changedCrs: Annotated[
        Optional[List[TransactionNsCrGvkNames]],
        Field(description='List of changed CRs as part of the transaction'),
    ] = None
    dryRun: Annotated[
        Optional[bool], Field(description='True if the transaction was not committed')
    ] = None
    generalErrors: Annotated[
        Optional[List[str]],
        Field(description='List of general errors while running the transaction'),
    ] = None
    inputCrs: Annotated[
        Optional[List[TransactionInputCr]],
        Field(description='List of input CRs from the transaction'),
    ] = None
    intentsRun: Annotated[
        Optional[List[TransactionIntentResult]],
        Field(description='List of intents which ran as part of the transaction'),
    ] = None
    nodesWithConfigChanges: Annotated[
        Optional[List[TransactionNodeResult]],
        Field(
            description='List of nodes with configuration changes from the transaction'
        ),
    ] = None
    state: Annotated[
        Optional[str], Field(description='The state of the transaction')
    ] = None
    success: Annotated[
        Optional[bool], Field(description='True if the CR was successfully applied')
    ] = None


class Transaction(BaseModel):
    crs: Annotated[
        List[TransactionCr],
        Field(description='List of CRs to include in the transaction'),
    ]
    description: Annotated[
        str, Field(description='Description/commit message for the transaction')
    ]
    dryRun: Annotated[
        bool,
        Field(
            description='If true the transaction will not be committed and will run in dry run mode.  If false the\ntransaction will be committed'
        ),
    ]
    resultType: Annotated[
        Optional[str],
        Field(description='The type of result - errors only, normal, or debug'),
    ] = None
    retain: Annotated[
        Optional[bool],
        Field(
            description='retain after results fetched - e.g. after call to get transaction result'
        ),
    ] = None
