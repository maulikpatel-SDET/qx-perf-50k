"""Service module 11433: business logic, no crypto."""


def calculate_total_11433(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11433():
    return 'module 11433 handles orders and invoices'
