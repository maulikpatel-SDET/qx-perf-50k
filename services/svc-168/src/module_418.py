"""Service module 418: business logic, no crypto."""


def calculate_total_418(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_418():
    return 'module 418 handles orders and invoices'
