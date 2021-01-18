from netaddr import IPNetwork, IPAddress
import robtex_python as robtex


def _communicating_with_domain(rule, communication, **kwargs):
    """
    Using the robtex project to query Internet data - current and stored.
    @note: Ideally we would like to navigate to both domain and IP and see that the output is the same, or even using
    simple nslookup to see if the domain translates to the IP, so there is very little chance to get the same IP that
    the user got. We do our best instead. This function is best effort, and prone to failures.
    @note: There is rate limit (a small one) for the robtex API.
    """
    domain = rule.argument
    ip = communication.host

    for record in (robtex.pdns_reverse(ip) or []):
        if 'rrname' in record and record['rrname'] == domain:
            return True

    for record in (robtex.pdns_forward(domain) or []):
        if 'rrtype' in record and record['rrtype'] == 'A' and 'rrdata' in record and record['rrdata'] == ip:
            return True

    ip_data = robtex.ip_query(ip)
    if ip_data:
        if 'status' in ip_data and ip_data['status'] == 'ok' and 'pas' in ip_data:
            for o_value in ip_data['pas']:
                if o_value == domain:
                    return True

    return False


def _multi_rules(rule, communication, **kwargs):
    if 'applying_rules' not in kwargs:
        return False

    applying_rules = kwargs['applying_rules']
    combined_rule_ids = rule.argument.split('-')

    all_device_ids_in_intersection = applying_rules[combined_rule_ids[0]]
    for rule_id in combined_rule_ids[1:]:
        if rule_id in applying_rules:
            all_device_ids_in_intersection = all_device_ids_in_intersection.intersection(applying_rules[rule_id])

    if communication.device_id in all_device_ids_in_intersection:
        return True
    return False


RULES_VALIDATORS = {
    'communicating_protocol': lambda rule, communication, **kwargs: rule.argument == communication.protocol_name,
    'communicating_with': lambda rule, communication, **kwargs: rule.argument == communication.host,
    'communicating_with_subnet': lambda rule, communication, **kwargs: IPAddress(communication.host) in IPNetwork(
        rule.argument),
    'communicating_with_domain': _communicating_with_domain,
    'multi_rules': _multi_rules
}
