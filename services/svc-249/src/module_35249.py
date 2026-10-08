"""Service module 35249: business logic, no crypto."""


def calculate_total_35249(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35249():
    return 'module 35249 handles orders and invoices'
