"""Service module 15824: business logic, no crypto."""


def calculate_total_15824(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15824():
    return 'module 15824 handles orders and invoices'
