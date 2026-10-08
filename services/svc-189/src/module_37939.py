"""Service module 37939: business logic, no crypto."""


def calculate_total_37939(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37939():
    return 'module 37939 handles orders and invoices'
