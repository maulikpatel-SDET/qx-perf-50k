"""Service module 48836: business logic, no crypto."""


def calculate_total_48836(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48836():
    return 'module 48836 handles orders and invoices'
