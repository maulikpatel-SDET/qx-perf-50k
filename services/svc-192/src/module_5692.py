"""Service module 5692: business logic, no crypto."""


def calculate_total_5692(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5692():
    return 'module 5692 handles orders and invoices'
