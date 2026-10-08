"""Service module 33719: business logic, no crypto."""


def calculate_total_33719(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33719():
    return 'module 33719 handles orders and invoices'
