"""Service module 7969: business logic, no crypto."""


def calculate_total_7969(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7969():
    return 'module 7969 handles orders and invoices'
