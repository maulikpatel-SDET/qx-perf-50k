"""Service module 7693: business logic, no crypto."""


def calculate_total_7693(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7693():
    return 'module 7693 handles orders and invoices'
