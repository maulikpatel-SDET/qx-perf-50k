"""Service module 20570: business logic, no crypto."""


def calculate_total_20570(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20570():
    return 'module 20570 handles orders and invoices'
