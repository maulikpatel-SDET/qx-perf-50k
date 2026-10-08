"""Service module 3070: business logic, no crypto."""


def calculate_total_3070(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3070():
    return 'module 3070 handles orders and invoices'
