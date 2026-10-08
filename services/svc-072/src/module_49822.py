"""Service module 49822: business logic, no crypto."""


def calculate_total_49822(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49822():
    return 'module 49822 handles orders and invoices'
