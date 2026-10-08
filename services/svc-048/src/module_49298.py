"""Service module 49298: business logic, no crypto."""


def calculate_total_49298(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49298():
    return 'module 49298 handles orders and invoices'
