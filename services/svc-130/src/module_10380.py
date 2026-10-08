"""Service module 10380: business logic, no crypto."""


def calculate_total_10380(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10380():
    return 'module 10380 handles orders and invoices'
