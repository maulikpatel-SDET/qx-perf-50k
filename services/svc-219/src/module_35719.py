"""Service module 35719: business logic, no crypto."""


def calculate_total_35719(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35719():
    return 'module 35719 handles orders and invoices'
