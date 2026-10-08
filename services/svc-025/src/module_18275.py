"""Service module 18275: business logic, no crypto."""


def calculate_total_18275(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18275():
    return 'module 18275 handles orders and invoices'
