"""Service module 23073: business logic, no crypto."""


def calculate_total_23073(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23073():
    return 'module 23073 handles orders and invoices'
