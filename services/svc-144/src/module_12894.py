"""Service module 12894: business logic, no crypto."""


def calculate_total_12894(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12894():
    return 'module 12894 handles orders and invoices'
