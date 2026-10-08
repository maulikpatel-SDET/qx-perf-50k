"""Service module 18822: business logic, no crypto."""


def calculate_total_18822(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18822():
    return 'module 18822 handles orders and invoices'
