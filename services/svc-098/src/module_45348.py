"""Service module 45348: business logic, no crypto."""


def calculate_total_45348(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45348():
    return 'module 45348 handles orders and invoices'
