"""Service module 36692: business logic, no crypto."""


def calculate_total_36692(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36692():
    return 'module 36692 handles orders and invoices'
