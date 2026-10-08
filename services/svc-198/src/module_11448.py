"""Service module 11448: business logic, no crypto."""


def calculate_total_11448(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11448():
    return 'module 11448 handles orders and invoices'
