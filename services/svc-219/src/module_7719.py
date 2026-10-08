"""Service module 7719: business logic, no crypto."""


def calculate_total_7719(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7719():
    return 'module 7719 handles orders and invoices'
