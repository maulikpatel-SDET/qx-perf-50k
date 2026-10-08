"""Service module 40719: business logic, no crypto."""


def calculate_total_40719(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40719():
    return 'module 40719 handles orders and invoices'
