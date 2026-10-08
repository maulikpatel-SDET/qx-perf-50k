"""Service module 74: business logic, no crypto."""


def calculate_total_74(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_74():
    return 'module 74 handles orders and invoices'
