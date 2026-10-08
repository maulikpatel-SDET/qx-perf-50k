"""Service module 15561: business logic, no crypto."""


def calculate_total_15561(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15561():
    return 'module 15561 handles orders and invoices'
