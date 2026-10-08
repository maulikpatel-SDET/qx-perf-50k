"""Service module 15939: business logic, no crypto."""


def calculate_total_15939(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15939():
    return 'module 15939 handles orders and invoices'
