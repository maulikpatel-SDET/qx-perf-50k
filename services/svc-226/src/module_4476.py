"""Service module 4476: business logic, no crypto."""


def calculate_total_4476(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4476():
    return 'module 4476 handles orders and invoices'
