"""Service module 5824: business logic, no crypto."""


def calculate_total_5824(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5824():
    return 'module 5824 handles orders and invoices'
