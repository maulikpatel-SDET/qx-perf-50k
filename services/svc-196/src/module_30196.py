"""Service module 30196: business logic, no crypto."""


def calculate_total_30196(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30196():
    return 'module 30196 handles orders and invoices'
