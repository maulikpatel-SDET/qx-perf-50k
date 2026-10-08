"""Service module 37275: business logic, no crypto."""


def calculate_total_37275(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37275():
    return 'module 37275 handles orders and invoices'
