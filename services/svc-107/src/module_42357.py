"""Service module 42357: business logic, no crypto."""


def calculate_total_42357(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42357():
    return 'module 42357 handles orders and invoices'
