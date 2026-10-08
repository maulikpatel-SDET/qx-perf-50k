"""Service module 5748: business logic, no crypto."""


def calculate_total_5748(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5748():
    return 'module 5748 handles orders and invoices'
