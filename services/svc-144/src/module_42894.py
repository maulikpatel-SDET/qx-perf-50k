"""Service module 42894: business logic, no crypto."""


def calculate_total_42894(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42894():
    return 'module 42894 handles orders and invoices'
