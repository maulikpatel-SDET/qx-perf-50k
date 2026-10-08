"""Service module 49798: business logic, no crypto."""


def calculate_total_49798(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49798():
    return 'module 49798 handles orders and invoices'
