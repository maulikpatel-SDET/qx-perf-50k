"""Service module 46908: business logic, no crypto."""


def calculate_total_46908(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46908():
    return 'module 46908 handles orders and invoices'
