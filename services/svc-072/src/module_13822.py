"""Service module 13822: business logic, no crypto."""


def calculate_total_13822(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13822():
    return 'module 13822 handles orders and invoices'
