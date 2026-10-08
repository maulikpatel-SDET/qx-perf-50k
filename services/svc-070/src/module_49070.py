"""Service module 49070: business logic, no crypto."""


def calculate_total_49070(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49070():
    return 'module 49070 handles orders and invoices'
