"""Service module 17200: business logic, no crypto."""


def calculate_total_17200(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17200():
    return 'module 17200 handles orders and invoices'
