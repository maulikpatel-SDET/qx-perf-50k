"""Service module 11204: business logic, no crypto."""


def calculate_total_11204(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11204():
    return 'module 11204 handles orders and invoices'
