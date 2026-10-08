"""Service module 10159: business logic, no crypto."""


def calculate_total_10159(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10159():
    return 'module 10159 handles orders and invoices'
