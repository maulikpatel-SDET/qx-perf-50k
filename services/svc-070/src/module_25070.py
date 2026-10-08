"""Service module 25070: business logic, no crypto."""


def calculate_total_25070(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25070():
    return 'module 25070 handles orders and invoices'
