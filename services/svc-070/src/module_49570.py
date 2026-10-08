"""Service module 49570: business logic, no crypto."""


def calculate_total_49570(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49570():
    return 'module 49570 handles orders and invoices'
