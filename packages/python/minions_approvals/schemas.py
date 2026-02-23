"""
Minions Approvals SDK — Type Schemas
Custom MinionType schemas for Minions Approvals.
"""

from minions.types import FieldDefinition, FieldValidation, MinionType

approval_request_type = MinionType(
    id="approvals-approval-request",
    name="Approval request",
    slug="approval-request",
    description="A pending action waiting for explicit human approval before execution.",
    icon="🔐",
    schema=[
        FieldDefinition(name="title", type="string", label="title"),
        FieldDefinition(name="description", type="string", label="description"),
        FieldDefinition(name="requestedBy", type="string", label="requestedBy"),
        FieldDefinition(name="requestedAt", type="string", label="requestedAt"),
        FieldDefinition(name="requiredBy", type="string", label="requiredBy"),
        FieldDefinition(name="contextRefType", type="string", label="contextRefType"),
        FieldDefinition(name="contextRefId", type="string", label="contextRefId"),
        FieldDefinition(name="payload", type="string", label="payload"),
        FieldDefinition(name="decision", type="select", label="decision"),
        FieldDefinition(name="decidedBy", type="string", label="decidedBy"),
        FieldDefinition(name="decidedAt", type="string", label="decidedAt"),
        FieldDefinition(name="decisionNotes", type="string", label="decisionNotes"),
    ],
)

approval_policy_type = MinionType(
    id="approvals-approval-policy",
    name="Approval policy",
    slug="approval-policy",
    description="A rule defining when approval is required for a given action type.",
    icon="📜",
    schema=[
        FieldDefinition(name="name", type="string", label="name"),
        FieldDefinition(name="actionType", type="string", label="actionType"),
        FieldDefinition(name="condition", type="string", label="condition"),
        FieldDefinition(name="requiredApproverRole", type="string", label="requiredApproverRole"),
        FieldDefinition(name="isActive", type="boolean", label="isActive"),
    ],
)

audit_log_entry_type = MinionType(
    id="approvals-audit-log-entry",
    name="Audit log entry",
    slug="audit-log-entry",
    description="An immutable record of any action taken by a human or agent.",
    icon="🕵️",
    schema=[
        FieldDefinition(name="actorId", type="string", label="actorId"),
        FieldDefinition(name="actorType", type="select", label="actorType"),
        FieldDefinition(name="action", type="string", label="action"),
        FieldDefinition(name="contextRefType", type="string", label="contextRefType"),
        FieldDefinition(name="contextRefId", type="string", label="contextRefId"),
        FieldDefinition(name="timestamp", type="string", label="timestamp"),
        FieldDefinition(name="payload", type="string", label="payload"),
        FieldDefinition(name="ipAddress", type="string", label="ipAddress"),
    ],
)

custom_types: list[MinionType] = [
    approval_request_type,
    approval_policy_type,
    audit_log_entry_type,
]

