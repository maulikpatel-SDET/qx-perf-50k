"""Service module 18801: business logic, no crypto."""


def calculate_total_18801(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18801():
    return 'module 18801 handles orders and invoices'
