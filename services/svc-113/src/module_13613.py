"""Service module 13613: business logic, no crypto."""


def calculate_total_13613(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13613():
    return 'module 13613 handles orders and invoices'
