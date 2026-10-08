"""Service module 630: business logic, no crypto."""


def calculate_total_630(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_630():
    return 'module 630 handles orders and invoices'
