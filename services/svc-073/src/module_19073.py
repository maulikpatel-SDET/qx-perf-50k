"""Service module 19073: business logic, no crypto."""


def calculate_total_19073(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19073():
    return 'module 19073 handles orders and invoices'
