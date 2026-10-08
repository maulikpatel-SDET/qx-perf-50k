"""Service module 1415: business logic, no crypto."""


def calculate_total_1415(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1415():
    return 'module 1415 handles orders and invoices'
