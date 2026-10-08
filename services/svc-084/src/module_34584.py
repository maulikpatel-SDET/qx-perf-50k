"""Service module 34584: business logic, no crypto."""


def calculate_total_34584(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34584():
    return 'module 34584 handles orders and invoices'
