"""Service module 36275: business logic, no crypto."""


def calculate_total_36275(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36275():
    return 'module 36275 handles orders and invoices'
