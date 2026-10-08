"""Service module 44563: business logic, no crypto."""


def calculate_total_44563(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44563():
    return 'module 44563 handles orders and invoices'
