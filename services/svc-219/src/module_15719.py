"""Service module 15719: business logic, no crypto."""


def calculate_total_15719(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15719():
    return 'module 15719 handles orders and invoices'
