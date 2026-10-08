"""Service module 45275: business logic, no crypto."""


def calculate_total_45275(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45275():
    return 'module 45275 handles orders and invoices'
