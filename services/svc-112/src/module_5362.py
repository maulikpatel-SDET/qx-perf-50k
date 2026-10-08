"""Service module 5362: business logic, no crypto."""


def calculate_total_5362(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5362():
    return 'module 5362 handles orders and invoices'
