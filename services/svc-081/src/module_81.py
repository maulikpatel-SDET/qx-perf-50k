"""Service module 81: business logic, no crypto."""


def calculate_total_81(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_81():
    return 'module 81 handles orders and invoices'
