"""Service module 30570: business logic, no crypto."""


def calculate_total_30570(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30570():
    return 'module 30570 handles orders and invoices'
