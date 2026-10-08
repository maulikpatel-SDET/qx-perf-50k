"""Service module 21526: business logic, no crypto."""


def calculate_total_21526(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21526():
    return 'module 21526 handles orders and invoices'
