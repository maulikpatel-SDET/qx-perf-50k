"""Service module 38630: business logic, no crypto."""


def calculate_total_38630(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38630():
    return 'module 38630 handles orders and invoices'
