from netaddr import IPNetwork, IPAddress

RULES_VALIDATORS = {
    'communicating_protocol': lambda rule, communication: rule.argument == communication.protocol_name,
    'communicating_with': lambda rule, communication: rule.argument == communication.host,
    'communicating_with_subnet': lambda rule, communication: IPAddress(communication.host) in IPNetwork(rule.argument)
}