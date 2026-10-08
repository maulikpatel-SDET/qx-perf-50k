"""Service module 44969: business logic, no crypto."""


def calculate_total_44969(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44969():
    return 'module 44969 handles orders and invoices'
