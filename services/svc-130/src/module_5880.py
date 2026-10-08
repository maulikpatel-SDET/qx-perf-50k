"""Service module 5880: business logic, no crypto."""


def calculate_total_5880(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5880():
    return 'module 5880 handles orders and invoices'
