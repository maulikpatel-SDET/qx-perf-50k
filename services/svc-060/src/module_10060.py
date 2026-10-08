"""Service module 10060: business logic, no crypto."""


def calculate_total_10060(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10060():
    return 'module 10060 handles orders and invoices'
