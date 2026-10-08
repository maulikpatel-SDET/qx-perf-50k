"""Service module 9630: business logic, no crypto."""


def calculate_total_9630(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9630():
    return 'module 9630 handles orders and invoices'
