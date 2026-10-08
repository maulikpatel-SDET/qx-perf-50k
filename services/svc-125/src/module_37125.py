"""Service module 37125: business logic, no crypto."""


def calculate_total_37125(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37125():
    return 'module 37125 handles orders and invoices'
