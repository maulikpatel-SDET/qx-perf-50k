"""Service module 47827: business logic, no crypto."""


def calculate_total_47827(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47827():
    return 'module 47827 handles orders and invoices'
