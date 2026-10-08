"""Service module 1894: business logic, no crypto."""


def calculate_total_1894(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1894():
    return 'module 1894 handles orders and invoices'
