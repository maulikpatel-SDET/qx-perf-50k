"""Service module 20815: business logic, no crypto."""


def calculate_total_20815(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20815():
    return 'module 20815 handles orders and invoices'
