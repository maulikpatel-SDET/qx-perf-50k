"""Service module 798: business logic, no crypto."""


def calculate_total_798(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_798():
    return 'module 798 handles orders and invoices'
