"""Service module 1458: business logic, no crypto."""


def calculate_total_1458(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1458():
    return 'module 1458 handles orders and invoices'
