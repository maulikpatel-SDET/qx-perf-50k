"""Service module 45410: business logic, no crypto."""


def calculate_total_45410(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45410():
    return 'module 45410 handles orders and invoices'
