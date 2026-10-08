"""Service module 12073: business logic, no crypto."""


def calculate_total_12073(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12073():
    return 'module 12073 handles orders and invoices'
