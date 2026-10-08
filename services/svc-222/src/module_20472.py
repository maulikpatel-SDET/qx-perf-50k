"""Service module 20472: business logic, no crypto."""


def calculate_total_20472(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20472():
    return 'module 20472 handles orders and invoices'
