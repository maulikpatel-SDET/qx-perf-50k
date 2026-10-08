"""Service module 12181: business logic, no crypto."""


def calculate_total_12181(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12181():
    return 'module 12181 handles orders and invoices'
