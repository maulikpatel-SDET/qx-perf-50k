"""Service module 17357: business logic, no crypto."""


def calculate_total_17357(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17357():
    return 'module 17357 handles orders and invoices'
