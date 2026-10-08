"""Service module 45567: business logic, no crypto."""


def calculate_total_45567(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45567():
    return 'module 45567 handles orders and invoices'
