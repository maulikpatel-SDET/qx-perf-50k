"""Service module 11070: business logic, no crypto."""


def calculate_total_11070(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11070():
    return 'module 11070 handles orders and invoices'
