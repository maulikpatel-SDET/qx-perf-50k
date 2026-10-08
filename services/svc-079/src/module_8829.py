"""Service module 8829: business logic, no crypto."""


def calculate_total_8829(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8829():
    return 'module 8829 handles orders and invoices'
