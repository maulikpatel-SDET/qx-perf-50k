"""Service module 45547: business logic, no crypto."""


def calculate_total_45547(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45547():
    return 'module 45547 handles orders and invoices'
