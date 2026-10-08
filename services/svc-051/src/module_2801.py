"""Service module 2801: business logic, no crypto."""


def calculate_total_2801(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2801():
    return 'module 2801 handles orders and invoices'
