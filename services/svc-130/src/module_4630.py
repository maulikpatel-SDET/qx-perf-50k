"""Service module 4630: business logic, no crypto."""


def calculate_total_4630(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4630():
    return 'module 4630 handles orders and invoices'
