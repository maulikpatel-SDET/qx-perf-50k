"""Service module 31584: business logic, no crypto."""


def calculate_total_31584(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31584():
    return 'module 31584 handles orders and invoices'
