"""Service module 25719: business logic, no crypto."""


def calculate_total_25719(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25719():
    return 'module 25719 handles orders and invoices'
