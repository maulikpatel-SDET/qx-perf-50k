"""Service module 17942: business logic, no crypto."""


def calculate_total_17942(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17942():
    return 'module 17942 handles orders and invoices'
