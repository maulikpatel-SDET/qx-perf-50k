"""Service module 49073: business logic, no crypto."""


def calculate_total_49073(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49073():
    return 'module 49073 handles orders and invoices'
