"""Service module 45459: business logic, no crypto."""


def calculate_total_45459(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45459():
    return 'module 45459 handles orders and invoices'
