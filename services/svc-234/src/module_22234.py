"""Service module 22234: business logic, no crypto."""


def calculate_total_22234(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22234():
    return 'module 22234 handles orders and invoices'
