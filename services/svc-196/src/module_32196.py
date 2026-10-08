"""Service module 32196: business logic, no crypto."""


def calculate_total_32196(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32196():
    return 'module 32196 handles orders and invoices'
