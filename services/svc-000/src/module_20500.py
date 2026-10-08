"""Service module 20500: business logic, no crypto."""


def calculate_total_20500(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20500():
    return 'module 20500 handles orders and invoices'
