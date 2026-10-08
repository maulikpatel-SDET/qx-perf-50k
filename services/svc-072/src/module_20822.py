"""Service module 20822: business logic, no crypto."""


def calculate_total_20822(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20822():
    return 'module 20822 handles orders and invoices'
