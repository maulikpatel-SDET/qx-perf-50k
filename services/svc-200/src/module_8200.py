"""Service module 8200: business logic, no crypto."""


def calculate_total_8200(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8200():
    return 'module 8200 handles orders and invoices'
