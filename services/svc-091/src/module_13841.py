"""Service module 13841: business logic, no crypto."""


def calculate_total_13841(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13841():
    return 'module 13841 handles orders and invoices'
