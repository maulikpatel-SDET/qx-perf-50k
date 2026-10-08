"""Service module 42638: business logic, no crypto."""


def calculate_total_42638(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42638():
    return 'module 42638 handles orders and invoices'
