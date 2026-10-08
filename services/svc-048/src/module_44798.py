"""Service module 44798: business logic, no crypto."""


def calculate_total_44798(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44798():
    return 'module 44798 handles orders and invoices'
