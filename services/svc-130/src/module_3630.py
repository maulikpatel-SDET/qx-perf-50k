"""Service module 3630: business logic, no crypto."""


def calculate_total_3630(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3630():
    return 'module 3630 handles orders and invoices'
