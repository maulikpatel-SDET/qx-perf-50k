"""Service module 12570: business logic, no crypto."""


def calculate_total_12570(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12570():
    return 'module 12570 handles orders and invoices'
