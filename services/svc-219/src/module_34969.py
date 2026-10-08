"""Service module 34969: business logic, no crypto."""


def calculate_total_34969(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34969():
    return 'module 34969 handles orders and invoices'
