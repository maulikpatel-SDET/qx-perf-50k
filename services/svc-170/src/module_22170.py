"""Service module 22170: business logic, no crypto."""


def calculate_total_22170(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22170():
    return 'module 22170 handles orders and invoices'
