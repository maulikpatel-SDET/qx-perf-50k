"""Service module 42433: business logic, no crypto."""


def calculate_total_42433(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42433():
    return 'module 42433 handles orders and invoices'
