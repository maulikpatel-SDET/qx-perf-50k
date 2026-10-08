"""Service module 24521: business logic, no crypto."""


def calculate_total_24521(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24521():
    return 'module 24521 handles orders and invoices'
