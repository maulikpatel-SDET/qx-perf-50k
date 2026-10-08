"""Service module 43275: business logic, no crypto."""


def calculate_total_43275(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43275():
    return 'module 43275 handles orders and invoices'
