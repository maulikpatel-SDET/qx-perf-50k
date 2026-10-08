"""Service module 30179: business logic, no crypto."""


def calculate_total_30179(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30179():
    return 'module 30179 handles orders and invoices'
