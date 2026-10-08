"""Service module 44570: business logic, no crypto."""


def calculate_total_44570(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44570():
    return 'module 44570 handles orders and invoices'
