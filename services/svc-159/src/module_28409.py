"""Service module 28409: business logic, no crypto."""


def calculate_total_28409(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28409():
    return 'module 28409 handles orders and invoices'
