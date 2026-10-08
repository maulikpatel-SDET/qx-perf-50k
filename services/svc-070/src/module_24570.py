"""Service module 24570: business logic, no crypto."""


def calculate_total_24570(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24570():
    return 'module 24570 handles orders and invoices'
