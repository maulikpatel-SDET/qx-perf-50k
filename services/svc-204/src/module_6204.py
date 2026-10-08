"""Service module 6204: business logic, no crypto."""


def calculate_total_6204(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6204():
    return 'module 6204 handles orders and invoices'
