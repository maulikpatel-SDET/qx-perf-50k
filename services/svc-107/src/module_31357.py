"""Service module 31357: business logic, no crypto."""


def calculate_total_31357(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31357():
    return 'module 31357 handles orders and invoices'
