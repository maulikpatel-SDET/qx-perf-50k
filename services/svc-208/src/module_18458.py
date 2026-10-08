"""Service module 18458: business logic, no crypto."""


def calculate_total_18458(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18458():
    return 'module 18458 handles orders and invoices'
