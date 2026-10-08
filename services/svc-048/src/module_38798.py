"""Service module 38798: business logic, no crypto."""


def calculate_total_38798(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38798():
    return 'module 38798 handles orders and invoices'
