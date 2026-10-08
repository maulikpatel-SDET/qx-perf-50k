"""Service module 45719: business logic, no crypto."""


def calculate_total_45719(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45719():
    return 'module 45719 handles orders and invoices'
