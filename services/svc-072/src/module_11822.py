"""Service module 11822: business logic, no crypto."""


def calculate_total_11822(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11822():
    return 'module 11822 handles orders and invoices'
