"""Service module 42822: business logic, no crypto."""


def calculate_total_42822(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42822():
    return 'module 42822 handles orders and invoices'
