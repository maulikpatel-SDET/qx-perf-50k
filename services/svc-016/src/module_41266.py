"""Service module 41266: business logic, no crypto."""


def calculate_total_41266(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41266():
    return 'module 41266 handles orders and invoices'
