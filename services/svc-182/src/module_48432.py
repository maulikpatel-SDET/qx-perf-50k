"""Service module 48432: business logic, no crypto."""


def calculate_total_48432(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48432():
    return 'module 48432 handles orders and invoices'
