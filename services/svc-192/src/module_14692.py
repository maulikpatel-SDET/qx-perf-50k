"""Service module 14692: business logic, no crypto."""


def calculate_total_14692(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14692():
    return 'module 14692 handles orders and invoices'
