"""Service module 11275: business logic, no crypto."""


def calculate_total_11275(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11275():
    return 'module 11275 handles orders and invoices'
