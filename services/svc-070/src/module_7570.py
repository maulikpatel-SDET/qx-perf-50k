"""Service module 7570: business logic, no crypto."""


def calculate_total_7570(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7570():
    return 'module 7570 handles orders and invoices'
