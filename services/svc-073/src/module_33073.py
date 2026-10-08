"""Service module 33073: business logic, no crypto."""


def calculate_total_33073(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33073():
    return 'module 33073 handles orders and invoices'
