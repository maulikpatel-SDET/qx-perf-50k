"""Service module 18533: business logic, no crypto."""


def calculate_total_18533(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18533():
    return 'module 18533 handles orders and invoices'
