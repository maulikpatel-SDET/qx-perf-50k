"""Service module 3399: business logic, no crypto."""


def calculate_total_3399(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3399():
    return 'module 3399 handles orders and invoices'
