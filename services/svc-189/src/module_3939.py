"""Service module 3939: business logic, no crypto."""


def calculate_total_3939(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3939():
    return 'module 3939 handles orders and invoices'
