"""Service module 18070: business logic, no crypto."""


def calculate_total_18070(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18070():
    return 'module 18070 handles orders and invoices'
