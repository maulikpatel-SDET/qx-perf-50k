"""Service module 35692: business logic, no crypto."""


def calculate_total_35692(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35692():
    return 'module 35692 handles orders and invoices'
