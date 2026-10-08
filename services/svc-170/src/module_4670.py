"""Service module 4670: business logic, no crypto."""


def calculate_total_4670(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4670():
    return 'module 4670 handles orders and invoices'
