"""Service module 26448: business logic, no crypto."""


def calculate_total_26448(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26448():
    return 'module 26448 handles orders and invoices'
