"""Service module 12822: business logic, no crypto."""


def calculate_total_12822(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12822():
    return 'module 12822 handles orders and invoices'
