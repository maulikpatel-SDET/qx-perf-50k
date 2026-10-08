"""Service module 9570: business logic, no crypto."""


def calculate_total_9570(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9570():
    return 'module 9570 handles orders and invoices'
