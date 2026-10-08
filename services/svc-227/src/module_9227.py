"""Service module 9227: business logic, no crypto."""


def calculate_total_9227(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9227():
    return 'module 9227 handles orders and invoices'
