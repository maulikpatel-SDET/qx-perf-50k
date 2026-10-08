"""Service module 9073: business logic, no crypto."""


def calculate_total_9073(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9073():
    return 'module 9073 handles orders and invoices'
