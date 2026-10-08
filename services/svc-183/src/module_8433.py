"""Service module 8433: business logic, no crypto."""


def calculate_total_8433(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8433():
    return 'module 8433 handles orders and invoices'
