"""Service module 9138: business logic, no crypto."""


def calculate_total_9138(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9138():
    return 'module 9138 handles orders and invoices'
