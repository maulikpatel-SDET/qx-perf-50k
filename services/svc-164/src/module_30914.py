"""Service module 30914: business logic, no crypto."""


def calculate_total_30914(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30914():
    return 'module 30914 handles orders and invoices'
