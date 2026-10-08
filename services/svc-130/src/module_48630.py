"""Service module 48630: business logic, no crypto."""


def calculate_total_48630(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48630():
    return 'module 48630 handles orders and invoices'
