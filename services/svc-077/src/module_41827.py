"""Service module 41827: business logic, no crypto."""


def calculate_total_41827(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41827():
    return 'module 41827 handles orders and invoices'
