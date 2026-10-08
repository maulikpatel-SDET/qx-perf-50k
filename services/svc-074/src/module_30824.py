"""Service module 30824: business logic, no crypto."""


def calculate_total_30824(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30824():
    return 'module 30824 handles orders and invoices'
