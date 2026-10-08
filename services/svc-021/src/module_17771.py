"""Service module 17771: business logic, no crypto."""


def calculate_total_17771(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17771():
    return 'module 17771 handles orders and invoices'
