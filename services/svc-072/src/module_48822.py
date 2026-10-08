"""Service module 48822: business logic, no crypto."""


def calculate_total_48822(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48822():
    return 'module 48822 handles orders and invoices'
