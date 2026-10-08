"""Service module 35275: business logic, no crypto."""


def calculate_total_35275(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35275():
    return 'module 35275 handles orders and invoices'
