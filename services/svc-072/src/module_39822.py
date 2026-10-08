"""Service module 39822: business logic, no crypto."""


def calculate_total_39822(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39822():
    return 'module 39822 handles orders and invoices'
