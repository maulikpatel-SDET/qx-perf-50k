"""Service module 49159: business logic, no crypto."""


def calculate_total_49159(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49159():
    return 'module 49159 handles orders and invoices'
