"""Service module 22822: business logic, no crypto."""


def calculate_total_22822(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22822():
    return 'module 22822 handles orders and invoices'
