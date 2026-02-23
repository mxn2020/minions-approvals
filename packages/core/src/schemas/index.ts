/**
 * @module @minions-approvals/sdk/schemas
 * Custom MinionType schemas for Minions Approvals.
 */

import type { MinionType } from 'minions-sdk';

export const approvalrequestType: MinionType = {
  id: 'approvals-approval-request',
  name: 'Approval request',
  slug: 'approval-request',
  description: 'A pending action waiting for explicit human approval before execution.',
  icon: '🔐',
  schema: [
    { name: 'title', type: 'string', label: 'title' },
    { name: 'description', type: 'string', label: 'description' },
    { name: 'requestedBy', type: 'string', label: 'requestedBy' },
    { name: 'requestedAt', type: 'string', label: 'requestedAt' },
    { name: 'requiredBy', type: 'string', label: 'requiredBy' },
    { name: 'contextRefType', type: 'string', label: 'contextRefType' },
    { name: 'contextRefId', type: 'string', label: 'contextRefId' },
    { name: 'payload', type: 'string', label: 'payload' },
    { name: 'decision', type: 'select', label: 'decision' },
    { name: 'decidedBy', type: 'string', label: 'decidedBy' },
    { name: 'decidedAt', type: 'string', label: 'decidedAt' },
    { name: 'decisionNotes', type: 'string', label: 'decisionNotes' },
  ],
};

export const approvalpolicyType: MinionType = {
  id: 'approvals-approval-policy',
  name: 'Approval policy',
  slug: 'approval-policy',
  description: 'A rule defining when approval is required for a given action type.',
  icon: '📜',
  schema: [
    { name: 'name', type: 'string', label: 'name' },
    { name: 'actionType', type: 'string', label: 'actionType' },
    { name: 'condition', type: 'string', label: 'condition' },
    { name: 'requiredApproverRole', type: 'string', label: 'requiredApproverRole' },
    { name: 'isActive', type: 'boolean', label: 'isActive' },
  ],
};

export const auditlogentryType: MinionType = {
  id: 'approvals-audit-log-entry',
  name: 'Audit log entry',
  slug: 'audit-log-entry',
  description: 'An immutable record of any action taken by a human or agent.',
  icon: '🕵️',
  schema: [
    { name: 'actorId', type: 'string', label: 'actorId' },
    { name: 'actorType', type: 'select', label: 'actorType' },
    { name: 'action', type: 'string', label: 'action' },
    { name: 'contextRefType', type: 'string', label: 'contextRefType' },
    { name: 'contextRefId', type: 'string', label: 'contextRefId' },
    { name: 'timestamp', type: 'string', label: 'timestamp' },
    { name: 'payload', type: 'string', label: 'payload' },
    { name: 'ipAddress', type: 'string', label: 'ipAddress' },
  ],
};

export const customTypes: MinionType[] = [
  approvalrequestType,
  approvalpolicyType,
  auditlogentryType,
];

