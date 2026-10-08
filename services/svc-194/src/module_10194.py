"""Service module 10194: business logic, no crypto."""


def calculate_total_10194(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10194():
    return 'module 10194 handles orders and invoices'
