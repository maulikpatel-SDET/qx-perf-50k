"""Service module 23632: business logic, no crypto."""


def calculate_total_23632(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23632():
    return 'module 23632 handles orders and invoices'
