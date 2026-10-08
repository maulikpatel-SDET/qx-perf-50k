"""Service module 27939: business logic, no crypto."""


def calculate_total_27939(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27939():
    return 'module 27939 handles orders and invoices'
