"""Service module 1317: business logic, no crypto."""


def calculate_total_1317(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1317():
    return 'module 1317 handles orders and invoices'
