"""Service module 21275: business logic, no crypto."""


def calculate_total_21275(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21275():
    return 'module 21275 handles orders and invoices'
