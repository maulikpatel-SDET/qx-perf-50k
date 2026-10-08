"""Service module 22798: business logic, no crypto."""


def calculate_total_22798(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22798():
    return 'module 22798 handles orders and invoices'
