"""Service module 44822: business logic, no crypto."""


def calculate_total_44822(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44822():
    return 'module 44822 handles orders and invoices'
