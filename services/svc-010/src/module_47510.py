"""Service module 47510: business logic, no crypto."""


def calculate_total_47510(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47510():
    return 'module 47510 handles orders and invoices'
