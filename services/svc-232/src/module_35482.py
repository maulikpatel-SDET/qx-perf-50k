"""Service module 35482: business logic, no crypto."""


def calculate_total_35482(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35482():
    return 'module 35482 handles orders and invoices'
