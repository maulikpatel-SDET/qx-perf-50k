"""Service module 23710: business logic, no crypto."""


def calculate_total_23710(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23710():
    return 'module 23710 handles orders and invoices'
