"""Service module 7798: business logic, no crypto."""


def calculate_total_7798(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7798():
    return 'module 7798 handles orders and invoices'
