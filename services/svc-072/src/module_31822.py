"""Service module 31822: business logic, no crypto."""


def calculate_total_31822(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31822():
    return 'module 31822 handles orders and invoices'
