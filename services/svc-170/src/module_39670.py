"""Service module 39670: business logic, no crypto."""


def calculate_total_39670(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39670():
    return 'module 39670 handles orders and invoices'
