"""Service module 33939: business logic, no crypto."""


def calculate_total_33939(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33939():
    return 'module 33939 handles orders and invoices'
