"""Service module 31200: business logic, no crypto."""


def calculate_total_31200(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31200():
    return 'module 31200 handles orders and invoices'
