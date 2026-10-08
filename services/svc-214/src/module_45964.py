"""Service module 45964: business logic, no crypto."""


def calculate_total_45964(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45964():
    return 'module 45964 handles orders and invoices'
