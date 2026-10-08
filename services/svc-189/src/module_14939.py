"""Service module 14939: business logic, no crypto."""


def calculate_total_14939(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14939():
    return 'module 14939 handles orders and invoices'
