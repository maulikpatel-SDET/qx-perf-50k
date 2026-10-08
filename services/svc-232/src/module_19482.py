"""Service module 19482: business logic, no crypto."""


def calculate_total_19482(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19482():
    return 'module 19482 handles orders and invoices'
