"""Service module 5952: business logic, no crypto."""


def calculate_total_5952(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5952():
    return 'module 5952 handles orders and invoices'
