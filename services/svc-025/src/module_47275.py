"""Service module 47275: business logic, no crypto."""


def calculate_total_47275(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47275():
    return 'module 47275 handles orders and invoices'
