"""Service module 18482: business logic, no crypto."""


def calculate_total_18482(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18482():
    return 'module 18482 handles orders and invoices'
