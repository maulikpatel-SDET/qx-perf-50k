"""Service module 23824: business logic, no crypto."""


def calculate_total_23824(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23824():
    return 'module 23824 handles orders and invoices'
