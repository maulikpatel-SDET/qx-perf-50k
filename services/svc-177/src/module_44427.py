"""Service module 44427: business logic, no crypto."""


def calculate_total_44427(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44427():
    return 'module 44427 handles orders and invoices'
