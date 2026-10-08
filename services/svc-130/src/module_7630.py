"""Service module 7630: business logic, no crypto."""


def calculate_total_7630(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7630():
    return 'module 7630 handles orders and invoices'
