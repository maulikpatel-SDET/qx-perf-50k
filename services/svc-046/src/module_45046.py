"""Service module 45046: business logic, no crypto."""


def calculate_total_45046(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45046():
    return 'module 45046 handles orders and invoices'
