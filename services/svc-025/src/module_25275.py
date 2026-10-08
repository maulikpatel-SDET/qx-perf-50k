"""Service module 25275: business logic, no crypto."""


def calculate_total_25275(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25275():
    return 'module 25275 handles orders and invoices'
