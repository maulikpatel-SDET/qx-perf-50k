"""Service module 48311: business logic, no crypto."""


def calculate_total_48311(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48311():
    return 'module 48311 handles orders and invoices'
