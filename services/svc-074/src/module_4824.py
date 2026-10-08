"""Service module 4824: business logic, no crypto."""


def calculate_total_4824(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4824():
    return 'module 4824 handles orders and invoices'
