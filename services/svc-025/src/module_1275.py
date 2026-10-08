"""Service module 1275: business logic, no crypto."""


def calculate_total_1275(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1275():
    return 'module 1275 handles orders and invoices'
