"""Service module 32433: business logic, no crypto."""


def calculate_total_32433(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32433():
    return 'module 32433 handles orders and invoices'
