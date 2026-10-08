"""Service module 17275: business logic, no crypto."""


def calculate_total_17275(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17275():
    return 'module 17275 handles orders and invoices'
