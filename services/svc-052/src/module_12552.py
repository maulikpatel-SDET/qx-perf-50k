"""Service module 12552: business logic, no crypto."""


def calculate_total_12552(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12552():
    return 'module 12552 handles orders and invoices'
