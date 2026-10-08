"""Service module 49034: business logic, no crypto."""


def calculate_total_49034(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49034():
    return 'module 49034 handles orders and invoices'
