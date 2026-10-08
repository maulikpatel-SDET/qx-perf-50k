"""Service module 39798: business logic, no crypto."""


def calculate_total_39798(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39798():
    return 'module 39798 handles orders and invoices'
