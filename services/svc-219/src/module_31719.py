"""Service module 31719: business logic, no crypto."""


def calculate_total_31719(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31719():
    return 'module 31719 handles orders and invoices'
