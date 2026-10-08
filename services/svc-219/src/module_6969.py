"""Service module 6969: business logic, no crypto."""


def calculate_total_6969(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6969():
    return 'module 6969 handles orders and invoices'
