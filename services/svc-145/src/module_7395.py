"""Service module 7395: business logic, no crypto."""


def calculate_total_7395(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7395():
    return 'module 7395 handles orders and invoices'
