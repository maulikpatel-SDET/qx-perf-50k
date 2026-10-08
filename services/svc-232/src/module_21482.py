"""Service module 21482: business logic, no crypto."""


def calculate_total_21482(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21482():
    return 'module 21482 handles orders and invoices'
