"""Service module 16798: business logic, no crypto."""


def calculate_total_16798(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16798():
    return 'module 16798 handles orders and invoices'
