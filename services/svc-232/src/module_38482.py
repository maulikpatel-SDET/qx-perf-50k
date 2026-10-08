"""Service module 38482: business logic, no crypto."""


def calculate_total_38482(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38482():
    return 'module 38482 handles orders and invoices'
