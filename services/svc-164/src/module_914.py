"""Service module 914: business logic, no crypto."""


def calculate_total_914(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_914():
    return 'module 914 handles orders and invoices'
