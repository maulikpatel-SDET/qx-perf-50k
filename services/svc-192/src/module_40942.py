"""Service module 40942: business logic, no crypto."""


def calculate_total_40942(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40942():
    return 'module 40942 handles orders and invoices'
