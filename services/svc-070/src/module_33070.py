"""Service module 33070: business logic, no crypto."""


def calculate_total_33070(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33070():
    return 'module 33070 handles orders and invoices'
