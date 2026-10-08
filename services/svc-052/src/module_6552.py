"""Service module 6552: business logic, no crypto."""


def calculate_total_6552(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6552():
    return 'module 6552 handles orders and invoices'
