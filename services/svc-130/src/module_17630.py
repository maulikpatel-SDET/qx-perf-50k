"""Service module 17630: business logic, no crypto."""


def calculate_total_17630(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17630():
    return 'module 17630 handles orders and invoices'
