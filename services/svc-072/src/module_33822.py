"""Service module 33822: business logic, no crypto."""


def calculate_total_33822(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33822():
    return 'module 33822 handles orders and invoices'
