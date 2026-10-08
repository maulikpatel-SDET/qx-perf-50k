"""Service module 12632: business logic, no crypto."""


def calculate_total_12632(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12632():
    return 'module 12632 handles orders and invoices'
