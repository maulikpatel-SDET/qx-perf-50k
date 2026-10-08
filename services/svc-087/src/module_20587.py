"""Service module 20587: business logic, no crypto."""


def calculate_total_20587(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20587():
    return 'module 20587 handles orders and invoices'
