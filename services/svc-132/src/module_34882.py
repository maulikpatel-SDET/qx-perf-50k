"""Service module 34882: business logic, no crypto."""


def calculate_total_34882(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34882():
    return 'module 34882 handles orders and invoices'
