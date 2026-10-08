"""Service module 45469: business logic, no crypto."""


def calculate_total_45469(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45469():
    return 'module 45469 handles orders and invoices'
