"""Service module 31228: business logic, no crypto."""


def calculate_total_31228(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31228():
    return 'module 31228 handles orders and invoices'
