"""Service module 17281: business logic, no crypto."""


def calculate_total_17281(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17281():
    return 'module 17281 handles orders and invoices'
