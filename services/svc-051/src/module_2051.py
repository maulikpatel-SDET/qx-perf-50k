"""Service module 2051: business logic, no crypto."""


def calculate_total_2051(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2051():
    return 'module 2051 handles orders and invoices'
