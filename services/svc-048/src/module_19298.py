"""Service module 19298: business logic, no crypto."""


def calculate_total_19298(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19298():
    return 'module 19298 handles orders and invoices'
