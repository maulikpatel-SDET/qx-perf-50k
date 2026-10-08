"""Service module 49969: business logic, no crypto."""


def calculate_total_49969(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49969():
    return 'module 49969 handles orders and invoices'
