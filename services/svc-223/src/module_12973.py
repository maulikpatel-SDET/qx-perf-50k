"""Service module 12973: business logic, no crypto."""


def calculate_total_12973(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12973():
    return 'module 12973 handles orders and invoices'
