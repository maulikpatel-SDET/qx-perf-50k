"""Service module 2458: business logic, no crypto."""


def calculate_total_2458(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2458():
    return 'module 2458 handles orders and invoices'
