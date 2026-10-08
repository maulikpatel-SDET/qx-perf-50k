"""Service module 1942: business logic, no crypto."""


def calculate_total_1942(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1942():
    return 'module 1942 handles orders and invoices'
