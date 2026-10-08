"""Service module 47923: business logic, no crypto."""


def calculate_total_47923(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47923():
    return 'module 47923 handles orders and invoices'
