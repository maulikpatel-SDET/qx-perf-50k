"""Service module 42081: business logic, no crypto."""


def calculate_total_42081(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42081():
    return 'module 42081 handles orders and invoices'
