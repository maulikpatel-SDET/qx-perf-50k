"""Service module 38939: business logic, no crypto."""


def calculate_total_38939(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38939():
    return 'module 38939 handles orders and invoices'
