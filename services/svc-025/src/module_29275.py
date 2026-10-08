"""Service module 29275: business logic, no crypto."""


def calculate_total_29275(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29275():
    return 'module 29275 handles orders and invoices'
