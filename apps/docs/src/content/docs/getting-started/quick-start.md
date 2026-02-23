---
title: Quick Start
description: Get up and running with Minions Approvals in minutes
---

## TypeScript

```typescript
import { createClient } from '@minions-approvals/sdk';

const client = createClient();
console.log('Version:', client.version);
```

## Python

```python
from minions_approvals import create_client

client = create_client()
print(f"Version: {client['version']}")
```

## CLI

```bash
approvals info
```
