"""Service module 25679: business logic, no crypto."""


def calculate_total_25679(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25679():
    return 'module 25679 handles orders and invoices'
