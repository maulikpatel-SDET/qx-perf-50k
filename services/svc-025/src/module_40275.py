"""Service module 40275: business logic, no crypto."""


def calculate_total_40275(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40275():
    return 'module 40275 handles orders and invoices'
