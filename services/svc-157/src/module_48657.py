"""Service module 48657: business logic, no crypto."""


def calculate_total_48657(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48657():
    return 'module 48657 handles orders and invoices'
