"""Service module 13969: business logic, no crypto."""


def calculate_total_13969(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13969():
    return 'module 13969 handles orders and invoices'
