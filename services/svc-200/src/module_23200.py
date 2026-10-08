"""Service module 23200: business logic, no crypto."""


def calculate_total_23200(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23200():
    return 'module 23200 handles orders and invoices'
