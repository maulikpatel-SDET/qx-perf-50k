"""Service module 15299: business logic, no crypto."""


def calculate_total_15299(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15299():
    return 'module 15299 handles orders and invoices'
