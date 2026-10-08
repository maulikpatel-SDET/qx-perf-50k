"""Service module 20354: business logic, no crypto."""


def calculate_total_20354(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20354():
    return 'module 20354 handles orders and invoices'
