"""Service module 822: business logic, no crypto."""


def calculate_total_822(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_822():
    return 'module 822 handles orders and invoices'
