"""Service module 18549: business logic, no crypto."""


def calculate_total_18549(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18549():
    return 'module 18549 handles orders and invoices'
