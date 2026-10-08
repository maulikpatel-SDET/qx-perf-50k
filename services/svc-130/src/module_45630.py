"""Service module 45630: business logic, no crypto."""


def calculate_total_45630(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45630():
    return 'module 45630 handles orders and invoices'
