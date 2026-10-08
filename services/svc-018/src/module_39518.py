"""Service module 39518: business logic, no crypto."""


def calculate_total_39518(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39518():
    return 'module 39518 handles orders and invoices'
