"""Service module 25922: business logic, no crypto."""


def calculate_total_25922(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25922():
    return 'module 25922 handles orders and invoices'
