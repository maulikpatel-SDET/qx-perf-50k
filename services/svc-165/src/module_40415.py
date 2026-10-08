"""Service module 40415: business logic, no crypto."""


def calculate_total_40415(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40415():
    return 'module 40415 handles orders and invoices'
