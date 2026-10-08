"""Service module 38822: business logic, no crypto."""


def calculate_total_38822(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38822():
    return 'module 38822 handles orders and invoices'
