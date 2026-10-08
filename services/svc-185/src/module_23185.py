"""Service module 23185: business logic, no crypto."""


def calculate_total_23185(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23185():
    return 'module 23185 handles orders and invoices'
