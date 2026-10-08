"""Service module 21433: business logic, no crypto."""


def calculate_total_21433(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21433():
    return 'module 21433 handles orders and invoices'
