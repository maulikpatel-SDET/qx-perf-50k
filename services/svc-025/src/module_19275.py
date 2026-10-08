"""Service module 19275: business logic, no crypto."""


def calculate_total_19275(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19275():
    return 'module 19275 handles orders and invoices'
