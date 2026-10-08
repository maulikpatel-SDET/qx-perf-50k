"""Service module 13801: business logic, no crypto."""


def calculate_total_13801(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13801():
    return 'module 13801 handles orders and invoices'
