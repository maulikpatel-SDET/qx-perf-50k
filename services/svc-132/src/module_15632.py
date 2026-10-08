"""Service module 15632: business logic, no crypto."""


def calculate_total_15632(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15632():
    return 'module 15632 handles orders and invoices'
