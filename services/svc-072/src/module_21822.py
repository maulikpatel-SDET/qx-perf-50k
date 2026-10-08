"""Service module 21822: business logic, no crypto."""


def calculate_total_21822(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21822():
    return 'module 21822 handles orders and invoices'
