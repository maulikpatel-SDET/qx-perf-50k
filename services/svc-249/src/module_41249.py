"""Service module 41249: business logic, no crypto."""


def calculate_total_41249(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41249():
    return 'module 41249 handles orders and invoices'
