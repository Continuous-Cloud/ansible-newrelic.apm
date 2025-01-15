# newrelic.apm_dotnet 

Install the new relic dotnet apm agent

Required Minimum Ansible Version is 2.9


This role supports the following Operating Systems:

<b>Windows</b>
  - 2019
  - 2016
  - 2012
  

## Usage

This role can be included like any other role to install the New Relic Dotnet APM agent.

### Example
```
---
- name: example
  hosts: localhost
  roles:
  - newrelic.apm.dotnet
    vars:
      dotnet_license_key: foo
```