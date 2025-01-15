# python 3 headers, required if submitting to Ansible
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.errors import AnsibleError
from ansible.plugins.lookup import LookupBase
from ansible_collections.newrelic.core.plugins.lookup_utils.agent_version_feed import (
    AgentVersionFeed
)

DOCUMENTATION = """
lookup: latest_dotnet_agent_version
author: Continuous Cloud
version_added: "1.0.0"
short_description: Lookup the latest available version of a NR dotnet APM agent
description:
    - Lookup the latest available version of a NR dotnet APM agent
options: {}
"""

USAGE = """
    - name: Lookup The Latest Dotnet Version
      debug:
        msg: "{{ lookup('newrelic.apm.latest_dotnet_agent_version') }}"
"""


class LookupModule(LookupBase):

    def run(self, terms, variables=None, **kwargs):
        version_feed_url = (
            "https://docs.newrelic.com/docs/release-notes/"
            "agent-release-notes/net-release-notes/feed.xml"
        )

        agent_version_feed = AgentVersionFeed()
        xml_feed = agent_version_feed.get_agent_release_feed(version_feed_url)
        latest_version = agent_version_feed.parse_latest_release_version_from_feed_xml(xml_feed)

        return [latest_version]
