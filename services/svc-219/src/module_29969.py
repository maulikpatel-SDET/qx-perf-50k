"""Service module 29969: business logic, no crypto."""


def calculate_total_29969(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29969():
    return 'module 29969 handles orders and invoices'
