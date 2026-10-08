"""Service module 18433: business logic, no crypto."""


def calculate_total_18433(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18433():
    return 'module 18433 handles orders and invoices'
