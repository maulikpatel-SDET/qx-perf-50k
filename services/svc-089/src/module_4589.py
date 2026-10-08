"""Service module 4589: business logic, no crypto."""


def calculate_total_4589(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4589():
    return 'module 4589 handles orders and invoices'
