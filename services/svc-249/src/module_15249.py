"""Service module 15249: business logic, no crypto."""


def calculate_total_15249(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15249():
    return 'module 15249 handles orders and invoices'
