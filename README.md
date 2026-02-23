# minions-approvals

**Approval requests, human decisions, and immutable audit logs**

Built on the [Minions SDK](https://github.com/mxn2020/minions).

---

## Quick Start

```bash
# TypeScript / Node.js
npm install @minions-approvals/sdk minions-sdk

# Python
pip install minions-approvals

# CLI (global)
npm install -g @minions-approvals/cli
```

---

## CLI

```bash
# Show help
approvals --help
```

---

## Python SDK

```python
from minions_approvals import create_client

client = create_client()
```

---

## Project Structure

```
minions-approvals/
  packages/
    core/           # TypeScript core library (@minions-approvals/sdk on npm)
    python/         # Python SDK (minions-approvals on PyPI)
    cli/            # CLI tool (@minions-approvals/cli on npm)
  apps/
    web/            # Playground web app
    docs/           # Astro Starlight documentation site
    blog/           # Blog
  examples/
    typescript/     # TypeScript usage examples
    python/         # Python usage examples
```

---

## Development

```bash
# Install dependencies
pnpm install

# Build all packages
pnpm run build

# Run tests
pnpm run test

# Type check
pnpm run lint
```

---

## Documentation

- Docs: [approvals.minions.help](https://approvals.minions.help)
- Blog: [approvals.minions.blog](https://approvals.minions.blog)
- App: [approvals.minions.wtf](https://approvals.minions.wtf)

---

## License

[MIT](LICENSE)
