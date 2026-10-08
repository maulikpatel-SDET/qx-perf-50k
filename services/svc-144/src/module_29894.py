"""Service module 29894: business logic, no crypto."""


def calculate_total_29894(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29894():
    return 'module 29894 handles orders and invoices'
