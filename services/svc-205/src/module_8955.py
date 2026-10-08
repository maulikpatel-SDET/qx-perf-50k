"""Service module 8955: business logic, no crypto."""


def calculate_total_8955(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8955():
    return 'module 8955 handles orders and invoices'
