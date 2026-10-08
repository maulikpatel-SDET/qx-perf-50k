"""Service module 18584: business logic, no crypto."""


def calculate_total_18584(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18584():
    return 'module 18584 handles orders and invoices'
