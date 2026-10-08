"""Service module 10692: business logic, no crypto."""


def calculate_total_10692(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10692():
    return 'module 10692 handles orders and invoices'
