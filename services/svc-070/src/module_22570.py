"""Service module 22570: business logic, no crypto."""


def calculate_total_22570(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22570():
    return 'module 22570 handles orders and invoices'
