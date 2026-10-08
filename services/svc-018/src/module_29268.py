"""Service module 29268: business logic, no crypto."""


def calculate_total_29268(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29268():
    return 'module 29268 handles orders and invoices'
