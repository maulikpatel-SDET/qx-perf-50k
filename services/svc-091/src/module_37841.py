"""Service module 37841: business logic, no crypto."""


def calculate_total_37841(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37841():
    return 'module 37841 handles orders and invoices'
