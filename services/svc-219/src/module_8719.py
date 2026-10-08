"""Service module 8719: business logic, no crypto."""


def calculate_total_8719(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8719():
    return 'module 8719 handles orders and invoices'
