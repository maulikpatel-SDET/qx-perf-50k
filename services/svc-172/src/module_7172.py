"""Service module 7172: business logic, no crypto."""


def calculate_total_7172(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7172():
    return 'module 7172 handles orders and invoices'
