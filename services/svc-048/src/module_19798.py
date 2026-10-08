"""Service module 19798: business logic, no crypto."""


def calculate_total_19798(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19798():
    return 'module 19798 handles orders and invoices'
