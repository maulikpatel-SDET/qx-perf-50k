"""Service module 49638: business logic, no crypto."""


def calculate_total_49638(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49638():
    return 'module 49638 handles orders and invoices'
