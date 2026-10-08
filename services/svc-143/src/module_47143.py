"""Service module 47143: business logic, no crypto."""


def calculate_total_47143(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47143():
    return 'module 47143 handles orders and invoices'
