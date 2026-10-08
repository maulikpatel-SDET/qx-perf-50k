"""Service module 23268: business logic, no crypto."""


def calculate_total_23268(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23268():
    return 'module 23268 handles orders and invoices'
