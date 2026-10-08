"""Service module 42070: business logic, no crypto."""


def calculate_total_42070(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42070():
    return 'module 42070 handles orders and invoices'
