"""Service module 11584: business logic, no crypto."""


def calculate_total_11584(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11584():
    return 'module 11584 handles orders and invoices'
