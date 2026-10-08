"""Service module 20275: business logic, no crypto."""


def calculate_total_20275(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20275():
    return 'module 20275 handles orders and invoices'
