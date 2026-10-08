"""Service module 36073: business logic, no crypto."""


def calculate_total_36073(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36073():
    return 'module 36073 handles orders and invoices'
