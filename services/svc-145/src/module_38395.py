"""Service module 38395: business logic, no crypto."""


def calculate_total_38395(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38395():
    return 'module 38395 handles orders and invoices'
