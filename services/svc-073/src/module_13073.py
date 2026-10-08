"""Service module 13073: business logic, no crypto."""


def calculate_total_13073(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13073():
    return 'module 13073 handles orders and invoices'
