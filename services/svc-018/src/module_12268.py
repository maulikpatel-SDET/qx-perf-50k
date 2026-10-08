"""Service module 12268: business logic, no crypto."""


def calculate_total_12268(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12268():
    return 'module 12268 handles orders and invoices'
