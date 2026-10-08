"""Service module 30073: business logic, no crypto."""


def calculate_total_30073(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30073():
    return 'module 30073 handles orders and invoices'
