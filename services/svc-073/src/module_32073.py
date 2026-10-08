"""Service module 32073: business logic, no crypto."""


def calculate_total_32073(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32073():
    return 'module 32073 handles orders and invoices'
