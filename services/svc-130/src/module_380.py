"""Service module 380: business logic, no crypto."""


def calculate_total_380(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_380():
    return 'module 380 handles orders and invoices'
