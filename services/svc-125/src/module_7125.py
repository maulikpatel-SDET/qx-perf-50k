"""Service module 7125: business logic, no crypto."""


def calculate_total_7125(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7125():
    return 'module 7125 handles orders and invoices'
