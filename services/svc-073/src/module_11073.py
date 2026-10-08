"""Service module 11073: business logic, no crypto."""


def calculate_total_11073(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11073():
    return 'module 11073 handles orders and invoices'
