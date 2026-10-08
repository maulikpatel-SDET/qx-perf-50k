"""Service module 18500: business logic, no crypto."""


def calculate_total_18500(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18500():
    return 'module 18500 handles orders and invoices'
