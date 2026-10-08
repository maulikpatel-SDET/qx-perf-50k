"""Service module 6939: business logic, no crypto."""


def calculate_total_6939(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6939():
    return 'module 6939 handles orders and invoices'
