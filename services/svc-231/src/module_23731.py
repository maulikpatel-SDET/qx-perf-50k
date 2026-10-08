"""Service module 23731: business logic, no crypto."""


def calculate_total_23731(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23731():
    return 'module 23731 handles orders and invoices'
