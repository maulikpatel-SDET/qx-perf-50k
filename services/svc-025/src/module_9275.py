"""Service module 9275: business logic, no crypto."""


def calculate_total_9275(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9275():
    return 'module 9275 handles orders and invoices'
