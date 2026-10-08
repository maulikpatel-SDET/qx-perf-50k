"""Service module 7070: business logic, no crypto."""


def calculate_total_7070(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7070():
    return 'module 7070 handles orders and invoices'
