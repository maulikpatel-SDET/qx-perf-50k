"""Service module 23822: business logic, no crypto."""


def calculate_total_23822(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23822():
    return 'module 23822 handles orders and invoices'
