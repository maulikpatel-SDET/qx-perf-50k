"""Service module 25564: business logic, no crypto."""


def calculate_total_25564(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25564():
    return 'module 25564 handles orders and invoices'
