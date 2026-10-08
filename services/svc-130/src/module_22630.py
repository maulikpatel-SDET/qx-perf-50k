"""Service module 22630: business logic, no crypto."""


def calculate_total_22630(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22630():
    return 'module 22630 handles orders and invoices'
