"""Service module 40073: business logic, no crypto."""


def calculate_total_40073(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40073():
    return 'module 40073 handles orders and invoices'
