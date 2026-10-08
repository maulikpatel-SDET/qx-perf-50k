"""Service module 15433: business logic, no crypto."""


def calculate_total_15433(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15433():
    return 'module 15433 handles orders and invoices'
