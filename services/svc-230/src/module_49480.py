"""Service module 49480: business logic, no crypto."""


def calculate_total_49480(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49480():
    return 'module 49480 handles orders and invoices'
