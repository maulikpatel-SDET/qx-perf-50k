"""Service module 40249: business logic, no crypto."""


def calculate_total_40249(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40249():
    return 'module 40249 handles orders and invoices'
