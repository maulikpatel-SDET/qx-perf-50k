"""Service module 29529: business logic, no crypto."""


def calculate_total_29529(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29529():
    return 'module 29529 handles orders and invoices'
