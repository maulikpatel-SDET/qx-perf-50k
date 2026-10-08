"""Service module 35570: business logic, no crypto."""


def calculate_total_35570(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35570():
    return 'module 35570 handles orders and invoices'
