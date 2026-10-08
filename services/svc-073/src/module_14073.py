"""Service module 14073: business logic, no crypto."""


def calculate_total_14073(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14073():
    return 'module 14073 handles orders and invoices'
