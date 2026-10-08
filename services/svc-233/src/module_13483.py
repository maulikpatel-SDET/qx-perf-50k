"""Service module 13483: business logic, no crypto."""


def calculate_total_13483(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13483():
    return 'module 13483 handles orders and invoices'
