"""Service module 17972: business logic, no crypto."""


def calculate_total_17972(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17972():
    return 'module 17972 handles orders and invoices'
