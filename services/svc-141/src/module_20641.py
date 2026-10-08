"""Service module 20641: business logic, no crypto."""


def calculate_total_20641(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20641():
    return 'module 20641 handles orders and invoices'
