"""Service module 5273: business logic, no crypto."""


def calculate_total_5273(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5273():
    return 'module 5273 handles orders and invoices'
