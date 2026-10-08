"""Service module 28275: business logic, no crypto."""


def calculate_total_28275(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28275():
    return 'module 28275 handles orders and invoices'
