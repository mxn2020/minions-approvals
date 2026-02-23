"""
Minions Approvals Python SDK

Approval requests, human decisions, and immutable audit logs
"""

__version__ = "0.1.0"


def create_client(**kwargs):
    """Create a client for Minions Approvals.

    Args:
        **kwargs: Configuration options.

    Returns:
        dict: Client configuration.
    """
    return {
        "version": __version__,
        **kwargs,
    }

from .schemas import *
