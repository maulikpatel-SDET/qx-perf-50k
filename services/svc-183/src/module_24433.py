"""Service module 24433: business logic, no crypto."""


def calculate_total_24433(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24433():
    return 'module 24433 handles orders and invoices'
