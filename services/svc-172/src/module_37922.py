"""Service module 37922: business logic, no crypto."""


def calculate_total_37922(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37922():
    return 'module 37922 handles orders and invoices'
